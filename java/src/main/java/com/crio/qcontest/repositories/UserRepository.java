package com.crio.qcontest.repositories;

 import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

import com.crio.qcontest.entities.User;

public class UserRepository implements IUserRepository{
    private final Map<Long,User> userMap;
    private Long autoIncrement = 1L;

    public UserRepository(){
        userMap = new HashMap<Long,User>();
    }

    // TODO: CRIO_TASK_MODULE_SERVICES
    // Complete the implementation of save method
    // Implementation must take care of the following cases:-
    // 1) Save a new user with unique ID to HashMap. ( Make use of AutoIncrement for unique ID)
    // 2) Increment autoIncrement variable once new user is saved.

    @Override
    public User save(User user) {
     return null;
    }

    // TODO: CRIO_TASK_MODULE_SERVICES
    // Complete the implementation of findAll method
    // Implementation must take care of the following cases:-
    // 1) Return all the users stored in HashMap.

    @Override
    public List<User> findAll() {
     return Collections.emptyList();
    }

    @Override
    public Optional<User> findById(Long id) {
        return Optional.ofNullable(userMap.get(id));
    }

    @Override
    public Optional<User> findByName(String name) {
    // Find an user which matches with the required name.
        return userMap.values().stream().filter(u -> u.getName().equals(name)).findFirst();
    }  
}
