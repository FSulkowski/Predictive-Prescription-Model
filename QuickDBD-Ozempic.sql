-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ytxgoq
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Cardio_Train" (
    "id" INT   NOT NULL,
    "age" INT   NOT NULL,
    "gender" INT   NOT NULL,
    "height" INT   NOT NULL,
    "weight" FLOAT   NOT NULL,
    "ap_hi" INT   NOT NULL,
    "ap_lo" INT   NOT NULL,
    "cholesterol" INT   NOT NULL,
    "gluc" INT   NOT NULL,
    "smoke" INT   NOT NULL,
    "alco" INT   NOT NULL,
    "active" INT   NOT NULL,
    "cardio" INT   NOT NULL,
    CONSTRAINT "pk_Cardio_Train" PRIMARY KEY (
        "id"
     )
);

