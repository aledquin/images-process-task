def write_frames(frame, memory_photos, step_rows, max_photos, output_video):
    for row, photo in reversed(list(enumerate(memory_photos))):
        memory_full = len(memory_photos) == max_photos
        if not memory_full:
            frame[0:row*step_rows, :] = photo[0:row*step_rows, :]
            break
        elif row == 0:
            frame[(max_photos-row-1) * step_rows: -1, :] = photo[(max_photos-row-1) * step_rows:-1, :]
        else:
            frame[(max_photos-row-1) * step_rows:(max_photos-row) * step_rows, :] = photo[(max_photos-row-1) * step_rows:(max_photos-row) * step_rows, :]
    output_video.write(frame)
    return frame, memory_photos
