package com.crio.qcontest.services;

import java.util.List;

import com.crio.qcontest.constants.UserOrder;
import com.crio.qcontest.entities.User;

public interface IUserService {
    User createUser(String name);
    List<User> getUsers(UserOrder userOrder);    
}