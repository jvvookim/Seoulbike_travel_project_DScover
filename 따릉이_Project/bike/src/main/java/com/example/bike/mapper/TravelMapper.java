package com.example.bike.mapper;

import com.example.bike.entity.Travel;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface TravelMapper {

    List<Travel> findAll();

}
