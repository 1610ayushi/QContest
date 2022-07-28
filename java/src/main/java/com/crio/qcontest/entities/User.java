package com.crio.qcontest.entities;

public class User {
    private final String name;
    private Integer totalScore;
    private final Long id;

    public User(String name, Long id) {
        this.name = name;
        this.id = id;
        this.totalScore = 100;
    }

    public User(String name) {
        this(name, null);
    }
    

    public String getName() {
        return name;
    }

    public Integer getTotalScore() {
        return totalScore;
    }

    public Long getId() {
        return id;
    }
    // TODO: CRIO_TASK_MODULE_ENTITIES
    // Complete the implementation of modifyScore method
    // Implementation must take care of the following cases:-
    // 1) Set an appropriate totalScore.
    // 2) Throw a Runtime Exception with an appropriate message for invalid score.

    public void modifyScore(Integer score){
    }

    @Override
    public String toString() {
        return "User [id=" + id + "]";
    }  
}
