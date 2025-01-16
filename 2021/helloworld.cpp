/*   -- Spoilers --
    AoC 2021 day 00 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <filesystem>

std::vector<std::string> parse_file(const std::string &path)
{
    std::vector<std::string> parsed_input;
    std::ifstream file(std::filesystem::current_path() / path);

    if (!file.is_open())
    {
        std::cerr << "Error opening file: " << path << std::endl;
        return parsed_input;
    }

    std::string line;
    while (std::getline(file, line))
    {
        parsed_input.push_back(line);
    }
    file.close();
    return parsed_input;
}

std::string part_one(const std::vector<std::string> &input)
{
    std::string answer = "Part one";
    return answer;
}

std::string part_two(const std::vector<std::string> &input)
{
    std::string answer = "Part two";
    return answer;
}

int main()
{
    std::string P1TEST = "0";
    std::string P2TEST = "0";
    std::vector<std::string> test_input = parse_file("00test.txt");
    std::vector<std::string> input = parse_file("00.txt");

    std::cout << part_one(test_input) << "  <--- Part 1 test (expected " << P1TEST << ")" << std::endl;
    std::cout << part_two(test_input) << "  <--- Part 2 test (expected " << P2TEST << ")" << std::endl;
    std::cout << std::endl;
    std::cout << part_one(input) << "   <--- Part 1 " << std::endl;
    std::cout << part_two(input) << "   <--- Part 2 " << std::endl;

    return 0;
}
