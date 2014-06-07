#include "FastaReader.h"
#include "BasicTypes.h"
#include "glwidget.h"
#include "UiVariables.h"
#include "SkittleUtil.h"

#include <string>
#include <cctype>


/** *********************
  FastaReader is the file reader for sequence files (FASTA format) usually ending in .fa.
  The first line starts with > and a name then the rest of the file is ACGT or acgt.  The
  character N is used to fill in unsequenced regions.  Capitalization is discarded by default
  since it is meant to mark "junk sequences".  All letters are capitalized for easy reading and
  so that equivalence checks A == a work in the rest of the program.

  FastaReader uses a progress bar dialog and is optimized for reading large files quickly.  It reads
  an entire file into memory, which makes reading the full 3GB human genome a big memory hog.
  FastaReader provides a string pointer (string*) to the rest of the program through the seq() method.
  The string is not ever copied, as it may be very large.  There are several unused read methods left
  over from experimentation with optimal memory management.

  FastaReader is created inside the constructor of glWidget so that there is a reader for
  every mdiChildWindow.  Each reader can only have one file open at a time.
  The actions:  openAction and addViewAction in MainWindow start a cascade that leads to the creation
  of a new FastaReader.

  *********************/

FastaReader::FastaReader()
{
    sequence = string("AATCGATCGTACGCTACGATCGCTACGCAGCTAGGACGGATT"); // random string of letters
    bytesInFile = 0;
    progressBar = NULL;
    cancelled = false;
}
FastaReader::~FastaReader()
{
    sequence.clear();
    sequence.resize(0);
}

bool FastaReader::readFile(string file)
{
    //Make sure that we were requested to open a file
    if(file.empty())
    {
        return false;
    }
    cout << file;

    //Parse the name of the chromosome from the file name and send it to glwidget to be stored
    storeChrName(file);

    //Clear out anything that may be left in the sequence string and set initial pad character
    sequence.clear();
    sequence = "";
    sequence.reserve(5);
    sequence = string(">");//extra character in front to make it 1-indexed instead of 0-indexed

    //Clear out anything that may be in the ifstream then open the new file
    wordfile.clear();
    wordfile.open(file.c_str(), ifstream::in | ifstream::binary);
    //See if we opened the file successfully
    if(wordfile.fail())
    {
        cerr << "Could not read the file. Either Skittle doesn't have file permissions or the file does not exist.";
        return false;
    }

    //Get how many characters are in the file
    wordfile.seekg(0, ios::beg);
    int begin = wordfile.tellg();
    wordfile.seekg(0, ios::end);
    int end = wordfile.tellg();
    bytesInFile = end - begin;

    //Discovered Reserve is different than malloc by creating a memory iterator
    //The iterator takes old size, then virtually allocates a new vector to new size while at the same time copying start/end memory to this new location
    //Then it destroys the old vector and walks through physical storage looking for a contiguous slot open, then dumps into the start and end location of new slot
    sequence.reserve(bytesInFile);

    //Return to the beginning of the file
    wordfile.seekg(0, ios::beg);
    //Skip the first line of the file as this is the chromosome name/info
    wordfile.ignore(500, '\n');

    //Read in the rest of the file
    char current;
    int i = 0;
    do
    {
        //Read the next character
        wordfile >> current;

        //If it is a letter, uppercase it
        current = upperCase(current);

        //if(current == 65 || current == 67 || current == 71 || current == 84 || current == 78) //A C G T N
        if(current != '\n' && current != '\r')
        {
            sequence.push_back(current);
        }

        i++;
    }
    while(!wordfile.eof() && !wordfile.fail());

    wordfile.close();

    cout << "Done loading file!";

    return true;
}

char FastaReader::upperCase(char& c)
{
    if( (int)c >= 97 && (int)c <= 122 )
        return (char)((int)c - 32);
    else
        return c;
}  

void FastaReader::storeChrName(string path)
{
    string name = trimPathFromFilename(path);
}

const string* FastaReader::seq()
{
    return &sequence;
}
