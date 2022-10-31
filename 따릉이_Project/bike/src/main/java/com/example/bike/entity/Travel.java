package com.example.bike.entity;

import lombok.Data;

@Data
public class Travel {
    private int id;

    private float latitude;

    private float longitude;

    private String nearest;

    private int rank;

    private String category;

    private float time;

    private String name;
}
