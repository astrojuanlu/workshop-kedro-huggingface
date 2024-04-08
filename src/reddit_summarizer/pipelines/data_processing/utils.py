def get_hashtags(text, mask_filler_model) -> list[str]:
    results = mask_filler_model(text.strip() + " #<mask>")

    hashtags = set()
    for ht_dict in results:
        hashtags.add(ht_dict["token_str"])

    if max(len(ht) for ht in hashtags) == 1:
        # Discard list of ugly hashtags
        return []

    return list(hashtags)


def get_summary(text, summarizer_model) -> str:
    summary = summarizer_model(text)[0]["summary_text"].strip()
    return summary
