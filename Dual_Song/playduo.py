from pydub import AudioSegment
from pydub.playback import play
from sys import argv, exit


def split_audio(left_song, right_song):
    """
    args:
        left_song: path of the left song to be played
        right_song: path of the right song to be played
    Process: Splits a stereo AudioSegment into two, one for each channel (Left/Right).
    Returns: A list of the new AudioSegment objects with the left channel and the right channel.
    """
    left_channel = AudioSegment.from_mp3(left_song)
    right_channel = AudioSegment.from_mp3(right_song)
    left_length = len(left_channel)
    right_lenght = len(right_channel)
    deference_between_channel = left_length - right_lenght
    print("left len: ", left_length)
    print("right len: ", right_lenght)
    print("deference_between_channel: ", deference_between_channel)
    print("left song loudness: ", left_channel.dBFS)
    print("right song loudness: ", right_channel.dBFS)
    if deference_between_channel > 0:
        final_left_channel = left_channel[:left_length]
        # After Finished song on right side we can append silence or left side song to right side.
        right_channel = right_channel.append(left_channel[right_lenght:], crossfade=0)
        # right_channel = right_channel.append(silence) ## if you need to add silence after finished song on right side
        right_lenght = len(right_channel)
        final_right_channel = right_channel[:right_lenght]
    elif deference_between_channel < 0:
        left_channel = left_channel.append(right_channel[left_length:], crossfade=0)
        # left_channel = left_channel.append(silence) ## if you need to add silence after finished song on left side
        left_length = len(left_channel)
        final_left_channel = left_channel[:left_length]
        final_right_channel = right_channel[:right_lenght]
    else:
        final_left_channel = left_channel[:left_length]
        final_right_channel = right_channel[:right_lenght]
    print("final_left_channel: ", len(final_left_channel))
    print("final_right_channel: ", len(final_right_channel))
    print("left song loudness: ", final_left_channel.rms)
    print("right song loudness: ", final_right_channel.rms)
    splitted_left_channel = final_left_channel.split_to_mono()
    splitted_right_channel = final_right_channel.split_to_mono()
    return splitted_left_channel, splitted_right_channel


def play_dual_song(left_song, right_song):
    """
    Play dual song at once. use headphone to enjoy this feature.
    """
    print("Please wait...!")
    left_channel, right_channel = split_audio(left_song, right_song)
    stereo_sound = AudioSegment.from_mono_audiosegments(left_channel[0], right_channel[1])
    print("Playing...!")
    play(stereo_sound)


if __name__ == '__main__':
    try:
        if not len(argv) == 3:
            exit("You must need to pass 2 song paths")
        # left_song = "(110) Alan Walker - Sing Me To Sleep - YouTube.mp3"
        # right_song = "(110) Alan Walker & Ava Max - Alone, Pt. II - YouTube.mp3"
        left_song = argv[1]
        right_song = argv[2]
        play_dual_song(left_song, right_song)
    except IOError:
        print("songs not found on given path")
    except KeyboardInterrupt:
        print("\nStopping the song & exit\n")