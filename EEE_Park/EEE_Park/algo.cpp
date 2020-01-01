#include "algo.h"
#include <ctime>
#include <cstdlib>
void carLeft() {
	string str = "python3 calculateTicket.py";
	const char* command = str.c_str();
	system(command);
}
//
//bool isGetTicket(time_t s_time) {
//	time_t time = std::time(0);
//	std::cout << difftime(time, s_time) << std::endl;
//	if (difftime(time, s_time) > TIME_OUT)
//		return true;
//	return false;
//}
//void sendWarning(string lp) {
//}
//void sendTicket(string lp) {
//	string img_path = "C:/Users/elia/PycharmProjects/EEE_Park/static/70-558-53.jpg";
//	string str = "python3 postTicket.py " + lp + " " + img_path + " " + NUM_CAMERA + " ";
//	const char* command = str.c_str();
//	system(command);
//}
//bool isCandidate(string lp, string img_name, const string num_camera) {
//	string str = "python3 checkIfCandidate.py " + lp + " " + img_name +" "+ num_camera + " ";
//	const char* command = str.c_str();
//	system(command);
//	//sendWarning(lp)
//}
//void carFadeIn() {
//	string lp = "1234567";
//	string img_path = "C:/Users/USER/Desktop/LP_RECOG/LP_TRY/LP_TRY/2car.png";
//	int camera_id = 1;
//	time_t s_time = std::time(0);
//	//isCandidate(lp);
//	candidate.push_back(ticketCandidate(lp, img_path, camera_id, s_time));
//}
//
//void carFadeOut() {
//	vector<string> leaveCars;
//	leaveCars.push_back("1234567");
//	/*for (size_t i = 0; i < leaveCars.size(); i++)
//	{
//		bool find = false;
//		time_t s_time;
//		for (size_t j = 0; j < candidate.size();j++)
//		{
//			if (candidate[j].lp == leaveCars[i]) {
//				find = true;
//				s_time = candidate[j].s_time;
//				break;
//			}
//		}
//		if (find && isGetTicket(s_time)) {
//			sendTicket(leaveCars[i]);
//		}
//	}
//	string lp = "1234567";*/
//	time_t s_time;//defult senario there is one car that enter to parking and get out
//	s_time = candidate[0].s_time;
//	if (isGetTicket(s_time)) {
//		sendTicket(leaveCars[0]);
//	}
//}