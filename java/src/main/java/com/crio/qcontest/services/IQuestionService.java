package com.crio.qcontest.services;

import java.util.List;

import com.crio.qcontest.entities.Level;
import com.crio.qcontest.entities.Question;

public interface IQuestionService {
    Question createQuestion(String title, Level level, Integer difficultyScore);
    List<Question> getAllQuestionLevelWise(Level level); 
}
