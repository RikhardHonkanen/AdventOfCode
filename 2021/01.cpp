#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <filesystem>

// Parse the input file into a vector of strings
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

// Part one logic
std::string part_one(const std::vector<std::string> &input)
{
    std::cout << "*input" << std::endl;
    std::string answer = "Part one";
    // Add your part one logic here
    return answer;
}

// Part two logic
std::string part_two(const std::vector<std::string> &input)
{
    std::string answer = "Part two";
    // Add your part two logic here
    return answer;
}

int main()
{
    // Placeholder for expected test results
    // std::string P1TEST = "0";
    // std::string P2TEST = "0";

    // Parse input files
    // std::vector<std::string> test_input = parse_file("0test.txt");
    std::vector<std::string> input = parse_file("1.txt");

    // Test and actual solutions
    // std::cout << "Part 1 Test: " << part_one(test_input) << " (expected " << P1TEST << ")" << std::endl;
    // std::cout << "Part 2 Test: " << part_two(test_input) << " (expected " << P2TEST << ")" << std::endl;
    // std::cout << std::endl;
    std::cout << "Part 1: " << part_one(input) << std::endl;
    std::cout << "Part 2: " << part_two(input) << std::endl;

    return 0;
}
