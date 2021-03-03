import cv2
import numpy as np
from write_frames import write_frames

video_name = 'test'
step_rows = 4

camera = cv2.VideoCapture(0)
camera_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
camera_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('{}.avi'.format(video_name), fourcc, 20, (camera_width, camera_height))

frame = np.zeros((camera_height, camera_width, 3), dtype='uint8')
max_photos = int(camera_height/step_rows)
memory_photos = []
while True:
    _, photo = camera.read()
    if len(memory_photos) == max_photos:
        memory_photos.append(photo)
        memory_photos.pop(0)
    else:
        memory_photos.append(photo)
    [frame, memory_photos] = write_frames(frame=frame, memory_photos=memory_photos,
                                          step_rows=step_rows, max_photos=max_photos,
                                          output_video=output_video)
    cv2.imshow('Tarea 1', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break
camera.release()
output_video.release()
cv2.destroyAllWindows()
