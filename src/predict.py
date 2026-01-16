CROP_KC = {
    "wheat": 0.7,
    "date_palm": 0.9,
    "vegetables": 1.05
}

def recommend_irrigation(et0, crop="date_palm"):
    kc = CROP_KC.get(crop, 0.9)
    return et0 * kc
