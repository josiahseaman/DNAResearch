#ifndef GTF_READER
#define GTF_READER

#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


class track_entry{ //copied from BasicTypes.h
public:
    int start;
    int stop;
    color col;
    string line;
    int index;
    track_entry(){
        start=0;
        stop = 0;
        col = color(0,0,0);
    }
    track_entry(int Start, int Stop, color C)
    {
        start = Start;
        stop = Stop;
        col = C;
    }
    track_entry(int Start, int Stop, color C, string Line)
    {
        start = Start;
        stop = Stop;
        col = C;
        line = Line;
    }
    bool operator < (track_entry& b)
    {
        if(start < b.start)
            return true;
        else if( start == b.start)
            return stop < b.stop;
        else
            return false;
    }
    bool isBlank()
    {
        return ( (start==0 && stop==0 && col.r == 0 && col.g == 0 && col.b == 0) );
    }
    string toString() const
    {
        return line;
    }
};



class GtfReader
{
public:
    string inputFilename;
    string chrName;

    GtfReader();
    vector<track_entry> readFile(string filename);
    string outputFile();
    void addBookmark(int start, int end);
    void determineOutputFile(string file);

private:
    bool initFile(string fileName);
    bool eq(string& str1, const char* str2);

    string outputFilename;
    ifstream file;
    int bytesInFile;//file size, but more specific
    int blockSize;
    QStringList getChromosomes();
};

#endif
