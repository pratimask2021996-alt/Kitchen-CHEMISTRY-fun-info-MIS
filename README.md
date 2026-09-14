# Kitchen Chemistry

A 6-page Flask site exploring the chemistry behind everyday cooking.

## Pages
- `/` — Home
- `/science` — 8 core concepts (Maillard, caramelization, emulsification, fermentation, acids/bases & leavening, protein denaturation, heat transfer, solutions/colloids/gels)
- `/experiments` — 5 safe kitchen experiments
- `/mysteries` — 7 click-to-reveal everyday questions
- `/quiz` — 6-question interactive quiz (client-side, no backend needed)
- `/creds` — project members + credit

## Running locally
```
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000

## Updating the Creds page later
Team photos live at:
- `static/images/harsh.jpg`
- `static/images/nayan.jpg`
- `static/images/shreyash.jpg`

These are placeholder avatars. To swap in a real photo, replace the file at the exact same path/name (same method used on the Obstacle Avoiding Bot site — upload the new file with the same name via GitHub/Render and it auto-deploys).

## Notes
- The "Created By" credit on the Creds page currently reads **@ Horizon creates.mis**, matching the tag used on the earlier Roht Wheeler site. Change it in `templates/creds.html` if you'd like something different.
- No database, no external image files besides the 3 member photos — everything else on the site (icons, hero illustration, diagrams) is inline SVG, so there's nothing else to replace before deploying.
