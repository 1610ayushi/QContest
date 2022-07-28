package com.crio.qcontest.services;

import java.util.List;

import com.crio.qcontest.entities.Level;
import com.crio.qcontest.entities.Question;
import com.crio.qcontest.repositories.IQuestionRepository;

public class QuestionService implements IQuestionService {

    private final IQuestionRepository questionRepository;

    public QuestionService(IQuestionRepository questionRepository) {
        this.questionRepository = questionRepository;
    }

    @Override
    public Question createQuestion(String title, Level level, Integer difficultyScore) {
        Question question = new Question(title, level, difficultyScore);
        return questionRepository.save(question);
    }

    @Override
    public List<Question> getAllQuestionLevelWise(Level level) {
        if(level == null){
            return questionRepository.findAll();
        }
        return questionRepository.findAllQuestionLevelWise(level);
    }
}
