package com.example.bike.service;

import com.example.bike.entity.Travel;
import com.example.bike.mapper.TravelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TravelService {

    @Autowired
    TravelMapper travelMapper;

    public List<Travel> findAll() {
        return travelMapper.findAll();
    }

}
