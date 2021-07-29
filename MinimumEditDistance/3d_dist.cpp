#include "3d_dist.h"


void _3d_dist::_2d_list::set_word(string file_word)
{
    word = file_word;
}

void _3d_dist::_2d_list::create_single_dp_table(string main_word)
{
    int x,y,i,j;
    x = main_word.length();
    y = word.length();
    

     for (int i = 0; i < x + 1; i++) { 
        vector<int> v1; 
  
        for (int j = 0; j < y + 1; j++) { 
            v1.push_back(0); 
             
        } 

        ij.push_back(v1); 
    } 


    for(i = 0 ; i < x + 1; ++i)
    {
        ij[i][0] = i;
    }

    for(i = 0 ; i < y + 1; ++i)
    {
        ij[0][i] = i;
    }



  
}

string _3d_dist::_2d_list::get_word() const
{
    return word;
}

void _3d_dist::_2d_list::print_single_table(string main_word) const
{
    int i,j;
    cout << "    ";
    for(i = 0 ; i < word.length() + 1; ++i)
    {
        if(i == word.length() - 1)
        {
            cout << word[i];
        }
        else
        {
            cout << word[i] << " ";
        }
    }
    cout << endl;

    for(i = 0 ; i < main_word.length() + 1; ++i)
    {
        if(i != 0 )
        {
            cout << main_word[i - 1] << " ";
        }
        else
        {
            cout << "  ";
        }
        
        for(j = 0 ; j < word.length() + 1; ++j)
        {
            cout << ij[i][j] << " ";
        }
        cout << endl;       
    }
}


int _3d_dist::_2d_list::find_single_min_dist(string main_word, int cost)
{
    int i, j, k;
    int min = 100;
    for(i = 1 ; i <= main_word.length() ; ++i)
    {
        for(j = 1 ; j <= word.length() ; ++j)
        {
            if(main_word[i - 1] == word[j - 1])
            {
                ij[i][j] = ij[i - 1][j - 1];
            }
            else 
            {
                ij[i][j] = 1 + _min(ij[i][j - 1], ij[i - 1][j], ij[i - 1][j - 1]);
            }

        for(k = 0 ; k <= word.length() ; ++k)
        {
            if(ij.at(i).at(k) < min)
            {
                min = ij.at(i).at(k);
            }
        }

        if(min > cost)
        {
            return -1;
        }
        min = 100;
            
        
        }
    }
   
    return ij[main_word.length()][word.length()];
}



int _3d_dist::_2d_list::_min(int a, int b, int c) const
{
    int smallest = a;
    if(smallest > b) smallest = b;
    if(smallest > c) smallest = c;

    return smallest;
}
double _3d_dist::_2d_list::find_single_ratio(string main_word) const
{
    int i,j;
    int zero_count = 0;
    //cout << "Word is " << word << endl;
    for(i = 1 ; i < main_word.length() ; ++i)
    { 
        for(j = 1 ; j < word.length() ; ++j)
        {
            if(ij[i][j] == 0)
            {
                zero_count++;
            }
        }
    }
    //cout << "Returning. " << (double)zero_count / (main_word.length() * word.length()) << endl;
    return 1 - ((double)zero_count / (main_word.length() * word.length()));
}



_3d_dist::_3d_dist()
{
    cout << "Default constructor." << endl;
}

_3d_dist::_3d_dist(const string &file_name, const string &inp_word)
{
        int i;
        main_word = inp_word;
       
        _2d_list entry;
        
        fstream infile;
        infile.open(file_name);
        if(!infile.good())
        {
            cerr << "Failed to open the file." << endl;
            exit(EXIT_FAILURE);
        }
        else
        {
            string line;
            while(getline(infile,line))
            {
                
                entry.set_word(line);

                k.push_back(entry);
            }
                
        }
        for(i = 0 ; i < WORD_COUNT ; ++i)
        {
            cout << k[i].get_word() << endl;
        }
}


void _3d_dist::create_whole_dp_table()
{
    int i;
    cout << "Vector size is " << k.size() << endl;
   
    for(i = 0 ; i < WORD_COUNT ; ++i)
    {
        k[i].create_single_dp_table(main_word);
        
    }
}

void _3d_dist::print_words() const
{
    int i;
    
    for(i = 0 ; i < k.size() ; ++i)
    {
        cout << k[i].get_word() << endl;
    }
}

void _3d_dist::print_whole_dp_table() const
{
    int i;

    for(i = 0 ; i < WORD_COUNT ; ++i)
    {   
        cout << endl;
        cout << i + 1 << ". word table: " << endl;
        k[i].print_single_table(main_word);
        cout << endl;
    }
    
}

void _3d_dist::print_specific_dp_table(int index) const
{
    cout << index << ". word table is: " << endl;
    k[index].print_single_table(main_word);
}


void _3d_dist::find_top_words() 
{   
    vector <string> words_list;
    int found = 0;
    int min = 30;
    int i,j;
    for(j = 0 ; j < 15 ; ++j)
    {
        for(i = 0 ; i < WORD_COUNT && found < 5  ; ++i)
        {
            if(k[i].find_single_min_dist(main_word, j) != -1 && std::find(words_list.begin(), words_list.end(), k[i].get_word()) == words_list.end())
            {
                found++;
                words_list.push_back(k[i].get_word());
                cout << "Found from cost " << j << endl;
                k[i].print_single_table(main_word);
            }
       
        }
    }
   
   
    
}

double _3d_dist:: find_total_ratio() const
{
    int i;
    double rates = 0.0;
    for(i = 0 ; i < WORD_COUNT ; ++i)
    {
        rates += k[i].find_single_ratio(main_word);
    }
    return rates / WORD_COUNT;
}

_3d_dist::_2d_list::_2d_list()
{
    //cout << "Default constructor of inner class." << endl;
}


bool isASCII (const std::string& s)
{
    return !std::any_of(s.begin(), s.end(), [](char c) { 
        return static_cast<unsigned char>(c) > 127; 
    });
}
