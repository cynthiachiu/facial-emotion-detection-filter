import cv2
import numpy as np
from fer import FER

def apply_mask(face: np.array, mask: np.array) -> np.array:
	mask_h, mask_w, _ = mask.shape
	face_h, face_w, _ = face.shape
	# Resize the mask to fit on face
	factor = min(face_h / mask_h, face_w / mask_w)
	new_mask_w = int(factor * mask_w)
	new_mask_h = int(factor * mask_h)
	new_mask_shape = (new_mask_w, new_mask_h)

	# Add mask to face - ensure mask is centered
	resized_mask = cv2.resize(mask, new_mask_shape)
	face_with_mask = face.copy()
	opaque_pixels = (resized_mask[:, :, 3] != 0)
	off_h = int((face_h - new_mask_h) / 2)
	off_w = int((face_w - new_mask_w) / 2)

	face_with_mask[off_h: off_h + new_mask_h, off_w: off_w + new_mask_w][opaque_pixels] = \
        resized_mask[:, :, :3][opaque_pixels]

	return face_with_mask

def main():
	cap = cv2.VideoCapture(0)

	# load mask
	mask0 = cv2.imread('assets/dog.png', cv2.IMREAD_UNCHANGED)
	mask1 = cv2.imread('assets/dalmation.png', cv2.IMREAD_UNCHANGED)
	mask2 = cv2.imread('assets/sheepdog.png', cv2.IMREAD_UNCHANGED)
	mask3 = cv2.imread('assets/terrier.png', cv2.IMREAD_UNCHANGED)
	mask4 = cv2.imread('assets/cat.png', cv2.IMREAD_UNCHANGED)
	mask5 = cv2.imread('assets/whitedog.png', cv2.IMREAD_UNCHANGED)
	masks = {"happy": (mask0, "Happy Doggo!"), "angry": (mask1, "Angry Dalmation"), 
			"neutral": (mask2, "Neutral Fox"),"surprise": (mask3, "Surprised Terrier"), 
			"disgust": (mask4, "Disgusted Kitty"), "fear": (mask4, "Scaredy Cat"), 
			"sad": (mask5, "Pouting Pupper"), "None": mask5}

	#detector = FER(mtcnn=True)
	detector = FER()

	while True:
		# init front face classifier
		cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
		
		# capture frame-by-frame
		ret, frame = cap.read()
		frame_h, frame_w, _ = frame.shape

		# Detect the emotion 
		result = detector.top_emotion(frame)
		print("result: ", result[0])
		detectedEmotion = result[0] 
		if detectedEmotion is None: 
			continue; 
		
		# convert to black and white
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		blackwhite = cv2.equalizeHist(gray)
		
		# detect all the faces in the image
		rects = cascade.detectMultiScale(
			blackwhite, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), 
			flags=cv2.CASCADE_SCALE_IMAGE)

		for x, y, w, h in rects:
			# crop a frame slightly larger than the face
			y0, y1 = int(y - 0.25*h), int(y + 0.75*h)
			x0, x1 = x, x + w

			# give up if the cropped frame would be out-of-bounds
			if x0 < 0 or y0 < 0 or x1 > frame_w or y1 > frame_h:
				continue

			# apply mask
			frame[y0: y1, x0: x1] = apply_mask(frame[y0: y1, x0: x1], masks[detectedEmotion][0])

			# Text overlay
			cv2.putText(frame, masks[detectedEmotion][1], (x0, y1 + 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

		# Display the resulting frame
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()
