#include <iostream>
using namespace std;

int main()
{
    int startHour, startMinute;
    cout << "Enter start time (hour minute): ";
    cin >> startHour >> startMinute;

    // Tổng số phút làm việc trong ngày (9 giờ 48 phút)
    int totalWorkMinutes = 9 * 60 + 48;

    int startTotal = startHour * 60 + startMinute;
    int endTotal = startTotal + totalWorkMinutes;

    int endHour = (endTotal / 60) % 24;
    int endMinute = endTotal % 60;

    cout << "You can leave work at: ";
    if (endHour < 10)
        cout << "0";
    cout << endHour << ":";
    if (endMinute < 10)
        cout << "0";
    cout << endMinute << endl;

    return 0;
}