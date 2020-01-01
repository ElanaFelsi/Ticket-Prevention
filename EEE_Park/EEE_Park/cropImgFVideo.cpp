/*#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <time.h>
#include <iostream>
using namespace std;
using namespace cv;
Mat detectAndDisplay(Mat frame);
CascadeClassifier face_cascade;
CascadeClassifier eyes_cascade;
CascadeClassifier smile_cascade;
int detectCandidate()
{
    VideoCapture capture;
    //-- 2. Read the video stream
    capture.open(0);
    if (!capture.isOpened())
    {
        cout << "--(!)Error opening video capture\n";
        return -1;
    }
    Mat frame;
    while (capture.read(frame))
    {
        if (frame.empty())
        {
            cout << "--(!) No captured frame -- Break!\n";
            break;
        }
        //-- 3. Apply the classifier to the frame

        clock_t tStart = clock();

        std::stringstream ss;
        ss << tStart;
        imwrite("frame_" + ss.str() + ".jpg", frame);
        printf("Time taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
        if (waitKey(10) == 27)
        {
            break; // escape
        }
    }
    return 0;
}*/