#include "3d_dist.h"
#include <locale>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        cerr << "Usage: ./exe filename" << endl;
        exit(EXIT_FAILURE);
    }
    string user_input;
    string file_name;
    cout <<"Please enter the word." << endl;
    cin >> user_input;
    string user_file_input = argv[1];
    if(!isASCII(user_input))
    {
        cerr << "Please enter ASCII characters. Turkish characters are not supported." << endl;
        exit(EXIT_FAILURE);
    }
    _3d_dist driver(user_file_input, user_input);

    driver.create_whole_dp_table();

    
    
    
    
    driver.print_whole_dp_table();
    cout << "top words:    " << endl;
    cout <<"\n\n\n\n\n";

     driver.find_top_words();
    cout << "Total occupied place is " <<driver.find_total_ratio() << endl;
    

    return 0;
}