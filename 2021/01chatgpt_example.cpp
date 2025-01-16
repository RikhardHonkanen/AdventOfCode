#include <iostream>
#include <fstream>
#include <vector>
#include <string>

// Function to parse input file into a vector of integers
std::vector<int> parse_file(const std::string &path)
{
    std::vector<int> numbers;
    std::ifstream file(path);
    if (!file.is_open())
    {
        std::cerr << "Error opening file: " << path << std::endl;
        return numbers;
    }

    int num;
    while (file >> num)
    { // Read integers line by line
        numbers.push_back(num);
    }
    return numbers;
}

// Function to calculate the number of increases
int count_increases(const std::vector<int> &depths)
{
    int count = 0;
    for (size_t i = 1; i < depths.size(); ++i)
    {
        if (depths[i] > depths[i - 1])
        {
            ++count;
        }
    }
    return count;
}

int main()
{
    std::vector<int> input = parse_file("01.txt");
    if (input.empty())
    {
        return 1; // Exit if no input was parsed
    }

    int increases = count_increases(input);
    std::cout << "Number of increases: " << increases << std::endl;

    return 0;
}