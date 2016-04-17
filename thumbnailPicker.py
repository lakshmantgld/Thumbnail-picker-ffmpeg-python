# - Python script to extract the thumbnails from video.
# - ffmpeg is used to extract the thumbnails.
# - This should be made as a cron job, called every 6 hours,
#  so that thumbnails, will be generated for any new videos added.

# Since the script is made as cron job, the routine thumbnailExtract() is written,
# to extract thumbnails only for those videos, whose thumbnail hasnt been extracted.
 
import subprocess, os;

# just give the parent directory there.
parentDirectory = '/Users/lakshman/vidd/'

# say the directory structure is like this:
#   -videos
#      |- ted
#      |- cricket
#      |- football
#      |- funny
#
# give the videos path to parentDirectory.


# the routine extracts thumbnails from all videos in the sub folders of the given directory
def thumbnailExtract():
    for dire in os.listdir(parentDirectory):
        if os.path.isdir(os.path.join(parentDirectory, dire)):
            directoryPath = os.path.join(parentDirectory, dire) + '/'

            # contains list of all videos in the given sub-folder.
            videoList = filter(lambda f: f.split('.')[-1] != 'png', os.listdir(directoryPath))

            # contains list of all thumbnails that are already present in the given sub-folder.
            thumbnailList = filter(lambda f: f.split('.')[-1] == 'png', os.listdir(directoryPath))

            for video in videoList:
                if (video + '.png') not in thumbnailList:
                    ffmpegp = subprocess.Popen(['ffmpeg', '-ss',
                                                '00:00:07.35', '-i',
                                                directoryPath + video, '-vframes',
                                                '1', directoryPath + video + '.png'])


thumbnailExtract()
