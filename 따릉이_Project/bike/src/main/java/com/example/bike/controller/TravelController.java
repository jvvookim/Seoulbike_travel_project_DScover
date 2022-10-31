package com.example.bike.controller;

import com.example.bike.entity.Travel;
import com.example.bike.service.TravelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class TravelController {

    @Autowired
    TravelService travelService;

    @GetMapping("/")
    public String root() {
        return "index";
    }

    @GetMapping("/findAll")
    public String findAll(ModelMap model) {
        List<Travel> list = travelService.findAll();
        System.out.println(list);
        model.addAttribute("list", list);
        return "test";
    }

    @GetMapping("/rests")
    public String getRests(ModelMap model, @RequestParam("currentLat") float currentLat, @RequestParam("currentLong") float currentLong) {
        model.addAttribute("currentLat", currentLat);
        model.addAttribute("currentLong", currentLong);
        return "test2";
    }
}
