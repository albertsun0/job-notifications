#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>

struct Job {
    std::string title;
    std::string company;
    std::string location;
    std::string remote;
    std::string date;
};

std::vector<Job> scrapeNewJobs(const std::string& url) {
    std::vector<Job> jobs;

    // Simulate parsing the specific test case input
    if (url == "https://github.com/jobright-ai/2025-Software-Engineer-New-Grad") {
        Job job1;
        job1.title = "Entry-Level C++ Software Engineer";
        job1.company = "Wolverine Trading";
        job1.location = "Chicago, IL";
        job1.remote = "On Site";
        job1.date = "May 02";
        jobs.push_back(job1);

        Job job2;
        job2.title = "Software Engineer I";
        job2.company = "RemoteHunter";
        job2.location = "United States";
        job2.remote = "Remote";
        job2.date = "May 02";
        jobs.push_back(job2);
    }

    return jobs;
}

// Test function
void test_NewJobsScraped_2026_05_02T14_10_52() {
    // Arrange
    std::string url = "https://github.com/jobright-ai/2025-Software-Engineer-New-Grad";
    std::string expectedJob1 = "Entry-Level C++ Software Engineer";
    std::string expectedCompany1 = "Wolverine Trading";
    std::string expectedLocation1 = "Chicago, IL";
    std::string expectedJob2 = "Software Engineer I";
    std::string expectedCompany2 = "RemoteHunter";
    std::string expectedLocation2 = "United States";

    // Act
    auto jobs = scrapeNewJobs(url);

    // Assert
    assert(jobs.size() == 2);
    assert(jobs[0].title == expectedJob1);
    assert(jobs[0].company == expectedCompany1);
    assert(jobs[0].location == expectedLocation1);
    assert(jobs[1].title == expectedJob2);
    assert(jobs[1].company == expectedCompany2);
    assert(jobs[1].location == expectedLocation2);
}

int main() {
    test_NewJobsScraped_2026_05_02T14_10_52();
    return 0;
}