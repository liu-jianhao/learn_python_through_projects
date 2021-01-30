import plistlib
from typing import Set, List, Any
from matplotlib import pyplot
import numpy as np


def find_common_tracks(fileNames):
    trackSets = []
    for fileName in fileNames:
        trackSet = set()
        with open(fileName, "rb") as file:
            pl = plistlib.load(file)
        tracks = pl["Tracks"]
        for trackID, track in tracks.items():
            trackName = track["Name"]
            trackSet.add(trackName)
        trackSets.append(trackSet)
    commonTracks = set.intersection(*trackSets)
    if len(commonTracks) > 0:
        f = open("common.txt", "wb")
        for val in commonTracks:
            s = "%s\n" % val
            f.write(s.encode("UTF-8"))
        f.close()
        print("%d common tracks found. "
              "Track names written to common.txt." % len(commonTracks))
    else:
        print("No common tracks")


def plot_stats(fileName):
    with open(fileName, "rb") as file:
        pl = plistlib.load(file)
    tracks = pl["Tracks"]

    ratings = []
    durations = []
    for trackID, track in tracks.items():
        try:
            ratings.append(track["Album Rating"])
            durations.append(track["Total Time"])
        except:
            pass

    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s." % fileName)
        return

    x = np.array(durations, np.int32)
    x = x/60000.0
    y = np.array(ratings, np.int32)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), -1, 110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')
    pyplot.subplot(2, 1, 2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')
    pyplot.show()


def main():
    find_common_tracks(["test-data/mymusic.xml"])
    plot_stats("test-data/mymusic.xml")


if __name__ == '__main__':
    main()
