#include <string>
#include <iostream>
#include <vector>
#define TIME_OUT 60
#define NUM_CAMERA "1"
using std::vector;
using std::string;
//class ticketCandidate {
//public:
//	ticketCandidate(string lp, string img_path, int camera_id, time_t time) :lp(lp), img_path(img_path),
//		camera_id(camera_id), s_time(time) {}
//	string lp;
//	string img_path;
//	int camera_id;
//	time_t s_time;
//};
//extern vector<ticketCandidate> candidate;
//void carFadeIn();
//void carFadeOut();
bool isGetTicket(time_t s_time);
void sendTicket(string lp);
bool isCandidate(string lp,string img_name,const string num_camera= NUM_CAMERA);
void carLeft();

