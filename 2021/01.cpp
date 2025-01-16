/*   -- Spoilers --
    AoC 2021 day 01 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <filesystem>

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

int count_increases_by_threes(const std::vector<int> &depths)
{
    int count = 0;
    for (size_t i = 0; i < depths.size() - 2; ++i)
    {
        int sweep_a = depths[i] + depths[i + 1] + depths[i + 2];
        int sweep_b = depths[i + 1] + depths[i + 2] + depths[i + 3];
        if (sweep_b > sweep_a)
        {
            ++count;
        }
    }
    return count;
}

std::string part_one(std::vector<int> &input)
{
    return std::to_string(count_increases(input));
}

std::string part_two(std::vector<int> &input)
{
    return std::to_string(count_increases_by_threes(input));
}

int main()
{
    std::string P1TEST = "7";
    std::string P2TEST = "5";
    std::vector<int> test_input = parse_file("01test.txt");
    std::vector<int> input = parse_file("01.txt");

    std::cout << part_one(test_input) << "  <--- Part 1 test (expected " << P1TEST << ")" << std::endl;
    std::cout << part_two(test_input) << "  <--- Part 2 test (expected " << P2TEST << ")" << std::endl;
    std::cout << std::endl;
    std::cout << part_one(input) << "   <--- Part 1 " << std::endl;
    std::cout << part_two(input) << "   <--- Part 2 " << std::endl;

    return 0;
}
