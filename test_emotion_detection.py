from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        stat1=emotion_detector("I am glad this happened")
        self.assertEqual(stat1['dominant_emotion'],'joy')
        stat2=emotion_detector("I am really mad about this")
        self.assertEqual(stat2['dominant_emotion'],'anger')
        state3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(state3['dominant_emotion'],'disgust')
        state4=emotion_detector("I am so sad about this")
        self.assertEqual(state4['dominant_emotion'],'sadness')
        state5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(state5['dominant_emotion'],'fear')
unittest.main()
