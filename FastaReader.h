#ifndef GEN_READER
#define GEN_READER

#include <stdlib.h>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct to_upper {
    int operator() ( int ch )
    {
        return std::toupper ( ch );
    }
};

class FastaReader
{
public:

    FastaReader();
    ~FastaReader();
    const string* seq();

    bool readFile(string name);

private:
    char upperCase(char& c);
    void storeChrName(string n);
    void setupProgressBar();
    string logo();

    ifstream wordfile;
    string sequence;
    int bytesInFile;//file size, but more specific
};

#endif
