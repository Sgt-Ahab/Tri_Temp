//Date of Creation: 01/03/2026
// Takes User Input, asks for unit, then conversion happens.
// User is given all three units of conversion (all in a three display display) enter new/quit loop.
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
double tempNum()
{
    double num;
    cout << "Enter a Number for Temperature: ";
    cin >> num;
    //logic is, if anything is not a number, characters + string becomes 0;
    //cout << num << endl; //Tester Flag --Number showed, letters made it still 0; use for input check.
    
    return num;
}
char getUnit()
{
    //ask for character that is the unit of reference to convert.
    char unit;
    cout << "Enter the unit of Temperature (K/C/F): ";
    cin >> unit;
    //cout << unit << endl; //Tester Flag --worked
    unit = toupper(unit);
    //cout << unit << endl; //toUpper Tester Flag --worked
    return unit;
}
bool validUnit(char u)
{
    if (u == 'C' || u == 'K' || u == 'F')
    {
        return true;
    }
    else
    {
        return false;
    }
}
bool validTempConv(double t, char u)
{
    //if-chain for temperature validation of C, F, K, as Physics refuse these.
    
    if (u == 'K')
    {
        if (t < 0.0)
        {
            return false;
        }
    }
    else if (u == 'F')
        {
        if (t < -459.67)
        {
            return false;
        }
        }
    else if (u == 'C')
        {
        if (t < -273.15)
        {
            return false;
        }
            
        }
    return true;

}
double toCelsius(double t, char u)
{
    //if check to make temperature convert to Celsius as a medium
    
    if (u == 'F')
    {
        t = (t - 32) * 5.0 / 9.0;
        return t;
    }
    if (u == 'K')
    {
        t = t - 273.15;
        return t;
    }
    if (u == 'C')
    {
        t = t;
        return t;
    }
    return t;
}
double cToF(double c)
{
    //takes Celsius and makes it Fahrenheit for display.
    c = c * 9.0 / 5.0 + 32.0;
    return c;
}
double cToK(double c)
{
    c = c + 273.15;
    return c;
}
void dispRes(double t, char u)
{
    string banner = "=+=+=+=+=+=+=+=+=+=+=+=+=\n";
    cout << setprecision(2) << fixed << endl;
    cout << banner << "Results:\n" << banner;
    if (u == 'F')
    {
        cout << endl << "|" << setw(5) << left << t << " " << u << " becomes: " << endl;
        cout << "|Celsius: " << setw(5) << left << toCelsius(t, u) << " C" << endl;
        cout << "|Kelvin: " << setw(6) << left << cToK(toCelsius(t, u)) << " K" << endl;
    }
    if (u == 'C')
    {
        cout << endl << "|" << setw(5) << left << t << " " << u << " becomes: " << endl;
        cout << "|Fahrenheit: " << setw(5) << left << cToF(t) << " F" << endl;
        cout << "|Kelvin: " << setw(6) << left << cToK(t) << " K" << endl;
    }
    if (u == 'K')
    {
        cout << endl << "|" << setw(5) << left << t << " " << u << " becomes: " << endl;
        cout << "|Celsius: " << setw(5) << left << toCelsius(t, u) << " C" << endl;
        cout << "|Fahrenheit: " << setw(5) << left << cToF(toCelsius(t, u)) << " F" << endl;
    }
}
char replayChar()
{
    char resp;
    cout << "|Would you like to convert a new temp? (Y/N): ";
    cin >> resp;
    //cout << resp << endl; //tester flag-- got the closer to show, bool wasn't reading
    resp = toupper(resp);
    //cout << "Modified: " << resp << endl; //tester flag--
    return resp;
}
bool replayCheck(char r)
{
    //character check for the bool,
    if (r == 'Y' || r == 'N')
    {
        return true;
    }
    else
    {
        return false;
    }
}


int main()
{
    bool isRunning = true;
    while (isRunning)
    {
        double input = tempNum();
        double temp = (input);
        char baseU = getUnit();
        while (!validUnit(baseU))
        {
            cout << "|ERROR: Not a unit. Enter (K/C/F).\n";
            baseU = getUnit();
        }
        while (!validTempConv(input, baseU))
        {
            cout << "|ERROR: Below Physical Limits. Retry\n";
            input = tempNum();
        }
        
        dispRes(input, baseU);

        char r = replayChar();
        while (!replayCheck(r))
        {
            cout << "|Error: Please enter Y or N.\n";
            r = replayChar();
        }
        if (r == 'N')
        {
            system("cls");
            cout << "|Thank you for using Tri-Temp!" << endl;
            isRunning = false;
        }
        else if (r == 'Y')
        {
            isRunning = true;
            system("cls");
        }
    }
}


