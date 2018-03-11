from PIL import Image
import face_recognition
import os
import sys,getopt

def find_and_save_face(web_file,face_file):
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(web_file)
    print(image.dtype)
    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top-30:bottom+30, left-30:right+30]
        pil_image = Image.fromarray(face_image)
        pil_image = pil_image.resize((256,256))
        pil_image.save(face_file)

opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file = ""
output_file = ""
for op, value in opts:
    if op == "-i":
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        print("preprocess.py -i inputfile -o outputfile")
        sys.exit()

if os.path.isdir(input_file):
    input_file = input_file.strip('/')
    list = os.listdir(input_file)
    for image in list:
        id_tag = image.find(".")
        name=image[0:id_tag]
        web_file = input_file + '/' +image
        face_file= output_file + '/'+name+'.jpg'
        try:
            find_and_save_face(web_file, face_file)
        except Exception, e:
            print(str(Exception))
            print(str(e))
elif os.path.isfile(input_file):
    try:
        find_and_save_face(input_file, output_file)
    except Exception, e:
        print(str(Exception))
        print(str(e))
else:
    print("Wrong parameter!")



