package com.crio.qcontest.services;

import java.util.List;

import com.crio.qcontest.entities.Contest;
import com.crio.qcontest.entities.Contestant;
import com.crio.qcontest.entities.Level;

public interface IContestService {
    Contest createContest(String title, Level level, String createdBy, Integer numQuestions);
    List<Contest> getAllContestLevelWise(Level level);
    Contestant createContestant(Long contestId, String userName);
    String deleteContestant(Long contestId, String userName);
    List<Contestant> runContest(Long contestId, String createdBy);
    List<Contestant> contestHistory(Long contestId);
}
