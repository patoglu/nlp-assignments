#include<iostream>
#include<string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
const int WORD_COUNT = 1000;
bool isASCII (const std::string& s);


class _3d_dist
{
    public:
        _3d_dist(); // Default cons
        _3d_dist(const string &file_name, const string &inp_word); // main const
        void print_words() const; // prints whole words
        void create_whole_dp_table(); // creates whole dp table
        void print_whole_dp_table() const; // print whole dp table
        void print_specific_dp_table(int index) const; // prints specific table
        void find_top_words() ; //finds the top words
        double find_total_ratio() const; //calcualtes the total ratio.
        
        class _2d_list
        {
            private:
                int _min(int a, int b, int c) const;
                vector<vector<int> > ij;
                string word;
            public:
                string get_word() const;
                void set_word(string file_word);
                _2d_list(/* args */);
                void create_single_dp_table(string main_word);
                void print_single_table(string main_word) const;
                int find_single_min_dist(string main_word, int cost);
                double find_single_ratio(string main_word) const;
                
        };
        
    
private:
    string main_word;
    vector <_2d_list> k;

};

