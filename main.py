import cv2
from detectingimages import train_data, detect_objects_in_photo, detect_objects_in_video, detect_objects_and_plot
from preprocessingimages import process_images_in_folder

def main():
    # Test detecting objects in a single image
    #image_path = "Dataset_2/test/images/WhatsApp-Video-2023-11-22-at-19_46_37_mp4-54_jpg.rf.37c622c6a79b700b0b2a707896b63ff1.jpg"
    #train_data()
    process_images_in_folder("images","images/processed_img") 
    image_path = "images/processed_img/Firearm-Safety-Rules-2.jpg"
    result_image_path = detect_objects_in_photo(image_path)
    
    print("Object detection result saved at:", result_image_path)

    # Test detecting objects in a video
    #video_path = "test_video.mp4"
    #result_video_path = detect_objects_in_video(video_path)
    #print("Object detection result video saved at:", result_video_path)

    # Test detecting objects in an image and displaying it
    #path_orig = "test_image.jpg"
    #detect_objects_and_plot(path_orig)

if __name__ == "__main__":
    main()
