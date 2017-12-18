import os


class Config:

    SAMPLE_NAME = 'video_sample2.mp4'
    YML_NAME = 'parking_lots_locs.yml'
    RECORDING_OUTPUT_NAME = 'recorded_sample.mp4'

    APP_DIR = os.path.dirname(os.path.abspath(__file__))

    DATA_DIR = os.path.join(APP_DIR, 'data')

    VIDEO_SAMPLE = os.path.join(DATA_DIR, SAMPLE_NAME)
    PL_LOCATIONS = os.path.join(DATA_DIR, YML_NAME)
    RECORDING_OUTPUT = os.path.join(DATA_DIR, RECORDING_OUTPUT_NAME)

    SAVE_VIDEO = False
    TEXT_OVERLAY = True
    PARKING_OVERLAY = True
    PARKING_ID_OVERLAY = True
    PARKING_DETECTION = True
    MOTION_DETECTION = False
    PEDESTRIAN_DETECTION = False
    MIN_AREA_MOTION_CONTOUR = 4000
    PARK_LAPLACIAN_TH = 1.5
    PARK_SEC_TO_WAIT = 5
    START_FRAME = 350
