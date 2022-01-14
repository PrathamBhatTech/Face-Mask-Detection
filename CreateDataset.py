'''
    Author: Pratham Bhat
            Pooshpal Baheti
    
    Description:    Used to create datasets for mask detection.
                    User can control time delay and the number of pictures per run.
'''


import os
import cv2
import uuid
import time
import asyncio
import tkinter as tk
import tkinter.font as tkFont
from mediapipe.python.solutions.face_detection import FaceDetection


# Get the path of this file
path = os.path.dirname(os.path.abspath(__file__))

folder_name = 'Dataset'

# If the required folders are not detected then they are created.
if not os.path.isdir(folder_name):
    os.mkdir(os.path.join(path, folder_name))
    os.makedirs(os.path.join(path, folder_name + '/with_mask'))
    os.makedirs(os.path.join(path, folder_name + '/without_mask'))    


# Face detection. It returns the bounding box coordinates of a face in the image and returns it.
def get_detection(frame):
    
    height, width, channel = frame.shape

    # Convert frame BGR to RGB colorspace
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detect results from the frame
    result = face_detection.process(imgRGB)
    
    # Extract data from result
    try:
        for count, detection in enumerate(result.detections):
            # Extract bounding box information  
            box = detection.location_data.relative_bounding_box
            x, y, w, h = int(box.xmin*width), int(box.ymin * height), int(box.width*width), int(box.height*height)

    except Exception as e:# If there is an exception print the exception for review and continue 
        print('ERROR: ', e)

    return x, y, w, h
    
async def SaveImage(img, category, timedelay):
    # Get the coordinates of the face that is detected in the image.
    x, y, w, h = get_detection(img)
    # Crop the face from the image using the coordinates from the get_detection function.
    crop_img = img[y-20:y+h+10, x-15:x+w+15]
    '''
    crop_img = cv2.resize(crop_img, (100, 100))
    crop_img = np.expand_dims(crop_img, axis=0)
    '''

    # Save the cropped image to the correct folder with a unique id as its name.
    filename = path + '/' + folder_name + "/" + category + "/" + str(uuid.uuid4()) + ".jpg"
    cv2.imwrite(filename, crop_img)

    # Show the cropped image.
    # cv2.imshow("crop img", crop_img)

    await asyncio.sleep(timedelay)


async def CreateDataset(timedelay, number_of_images, category):
    # Start capturing video from the webcam.
    # NOTE: If you want to use an external webcam replace 0 with 1
    cap = cv2.VideoCapture(0)

    print("Focusing camera. Please wait.")
    _, frame = cap.read()
    # This is to allow the camera to focus properly before collecting pictures.
    time.sleep(2)

    while number_of_images:
        
        _, frame = cap.read()

        # Show the frame
        # print("frame should be updated")
        cv2.imshow("frame", frame)

        try:
            if task.done():
                task = asyncio.create_task(SaveImage(frame, category, timedelay))
                number_of_images -= 1
        except:     #For 1st run
            task = asyncio.create_task(SaveImage(frame, category, timedelay))
            number_of_images -= 1

        
        
        await asyncio.sleep(0.1)

        # Waits until the number of images requested by the user is stored or until 'q' is pressed
        # and closes every opencv window
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


class App:
    def __init__(self, root):
        #setting title
        root.title("Mask Dataset Generator")

        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        #Labels
        Title_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=40)
        Title_Label["font"] = ft
        Title_Label["fg"] = "#333333"
        Title_Label["justify"] = "center"
        Title_Label["text"] = "Mask Dataset Generator"
        Title_Label.place(x=0,y=10,width=600,height=62)

        TimeDelay_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        TimeDelay_Label["font"] = ft
        TimeDelay_Label["fg"] = "#333333"
        TimeDelay_Label["justify"] = "center"
        TimeDelay_Label["text"] = "Time Delay: "
        TimeDelay_Label.place(x=120,y=160, width=150, height=37)

        NumberOfImages_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        NumberOfImages_Label["font"] = ft
        NumberOfImages_Label["fg"] = "#333333"
        NumberOfImages_Label["justify"] = "center"
        NumberOfImages_Label["text"] = "Number of images: "
        NumberOfImages_Label.place(x=80,y=210, width=250, height=37)

        TimeDelayUnit_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        TimeDelayUnit_Label["font"] = ft
        TimeDelayUnit_Label["fg"] = "#333333"
        TimeDelayUnit_Label["justify"] = "center"
        TimeDelayUnit_Label["text"] = "s"
        TimeDelayUnit_Label.place(x=370,y=160,width=40,height=40)


        #Entries
        self.TimeDelay_Entry=tk.Entry(root)
        self.TimeDelay_Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        self.TimeDelay_Entry["font"] = ft
        self.TimeDelay_Entry["fg"] = "#333333"
        self.TimeDelay_Entry["justify"] = "center"
        self.TimeDelay_Entry["text"] = "TimeDelay"
        self.TimeDelay_Entry["textvariable"] = "0.5"
        self.TimeDelay_Entry.insert(0, "0.2")      #Setting default values
        self.TimeDelay_Entry.place(x=265,y=165,width=100,height=30)

        self.NumberOfImages_Entry=tk.Entry(root)
        self.NumberOfImages_Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        self.NumberOfImages_Entry["font"] = ft
        self.NumberOfImages_Entry["fg"] = "#333333"
        self.NumberOfImages_Entry["justify"] = "center"
        self.NumberOfImages_Entry["text"] = "NumberOfImages"
        self.NumberOfImages_Entry.insert(0, "30")      #Setting default values
        self.NumberOfImages_Entry.place(x=325,y=215,width=100,height=30)


        #Buttons
        WithMask_Button=tk.Button(root)
        WithMask_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        WithMask_Button["font"] = ft
        WithMask_Button["fg"] = "#000000"
        WithMask_Button["justify"] = "center"
        WithMask_Button["text"] = "With Mask"
        WithMask_Button.place(x=70,y=300,width=200,height=60)
        WithMask_Button["command"] = self.WithMask_Button_Clicked

        WithoutMask_Button=tk.Button(root)
        WithoutMask_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        WithoutMask_Button["font"] = ft
        WithoutMask_Button["fg"] = "#000000"
        WithoutMask_Button["justify"] = "center"
        WithoutMask_Button["text"] = "Without Mask"
        WithoutMask_Button.place(x=330,y=300,width=200,height=60)
        WithoutMask_Button["command"] = self.WithoutMask_Button_Clicked


    def WithMask_Button_Clicked(self):
        self.CallCreateDataset('with_mask')

    def WithoutMask_Button_Clicked(self):
        self.CallCreateDataset('without_mask')


    def CallCreateDataset(self, category):
        # Get data from the entry labels.
        timedelay = float(self.TimeDelay_Entry.get())
        number_of_images = int(self.NumberOfImages_Entry.get())

        asyncio.run(CreateDataset(timedelay, number_of_images, category))



if __name__ == "__main__":
    # Create a face detection function with its minimum accuracy at 40%
    face_detection = FaceDetection(0.4)   


    # Initiate the tkinter window and set its values
    root = tk.Tk()
    app = App(root)

    root.mainloop()
