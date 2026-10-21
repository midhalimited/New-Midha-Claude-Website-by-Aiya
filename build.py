"""Generates the static Midha Limited website into ./site.

Each page is plain HTML (no build step needed on Cloudflare Pages).
Edit the content below and re-run:  python3 build.py
"""
import json, os, html, datetime

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
SITE = "https://midha.co.nz"
PHONE = "022 407 8603"
TEL = "+64224078603"
EMAIL = "midhalimited@gmail.com"
HOURS = "Mon–Sat 7:30am–6:00pm"
TODAY = datetime.date(2026, 10, 21).isoformat()
STANDARD = "AS/NZS 3760:2022"
MED_STD = "AS/NZS 3551"
FIRE_STD = "NZS 4503:2005"
MED_PATH = "/test-and-tag/medical-equipment-testing/"
FIRE_PATH = "/test-and-tag/fire-extinguisher-testing/"
EST = "Registered Electrical Service Technician"
FB_POST = "https://www.facebook.com/photo.php?fbid=122215666088570841&set=pb.61567125254358.-2207520000&type=3"

def next_draw(d):
    """Giveaway draws happen at the end of March, June, September and December."""
    for m, day in ((3, 31), (6, 30), (9, 30), (12, 31)):
        end = datetime.date(d.year, m, day)
        if end >= d:
            return end
    return datetime.date(d.year + 1, 3, 31)

NEXT_DRAW = next_draw(datetime.date.fromisoformat(TODAY)).strftime("%-d %B %Y")

e = html.escape

# ---------------------------------------------------------------- icons
def icon(name, size=24, color="currentColor"):
    paths = {
        "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8Z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
        "fan": '<circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-7 4-7s3 4-1 7"/><path d="M14 12c4 0 7 1 7 4s-4 3-7-1"/><path d="M12 14c0 4-1 7-4 7s-3-4 1-7"/><path d="M10 12c-4 0-7-1-7-4s4-3 7 1"/>',
        "bulb": '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V18h6v-1.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2Z"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
        "shield": '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
        "qr": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/>',
        "dollar": '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2.2 0 3 6 1.6 6 4.6 0 1.3-1.3 2.2-3 2.2-1.4 0-2.6-.6-3-1.6M12 6.5V8m0 8v1.5"/>',
        "leaf": '<path d="M11 20A7 7 0 0 1 4 13c0-6 7-9 16-9 0 9-3 16-9 16Z"/><path d="M4 20c4-4 7-6 11-8"/>',
        "home": '<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
        "plug": '<path d="M9 2v6M15 2v6"/><path d="M6 8h12v4a6 6 0 0 1-12 0Z"/><path d="M12 18v4"/>',
        "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>',
        "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8 2.3 2.3a4 4 0 0 0 2.4 2Z"/>',
        "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9Z"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "chev": '<path d="m6 9 6 6 6-6"/>',
        "cross": '<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M12 8v8M8 12h8"/>',
        "flame": '<path d="M12 22a7 7 0 0 0 7-7c0-3.5-2.2-5.6-3.6-8.6-.5 1.9-1.4 3.1-2.6 3.8C12.6 7 11.4 4.4 9 2.5 8.8 6.6 5 9.6 5 15a7 7 0 0 0 7 7Z"/><path d="M12 22a3 3 0 0 0 3-3c0-2-1.6-3-3-5-1.4 2-3 3-3 5a3 3 0 0 0 3 3Z"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{paths[name]}</svg>')

def pic(name, alt, w=800, cls="", sizes="(max-width: 860px) 100vw, 50vw", eager=False, big=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    srcset_webp = f"/assets/img/{name}-800.webp 800w" + (f", /assets/img/{name}-1600.webp 1600w" if big else "")
    srcset_jpg = f"/assets/img/{name}-800.jpg 800w" + (f", /assets/img/{name}-1600.jpg 1600w" if big else "")
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/webp" srcset="{srcset_webp}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-800.jpg" srcset="{srcset_jpg}" sizes="{sizes}" alt="{e(alt)}"{c} {load} decoding="async"></picture>')

# ---------------------------------------------------------------- shared data
SERVICES = [
    ("test-tag", "/test-and-tag/", "Test & Tag", "tag"),
    ("heat-pump", "/heat-pump-cleaning/", "Heat Pump Cleaning", "fan"),
    ("electrical", "/electrical-services/", "Electrical Services", "bulb"),
]
AREAS = [
    ("Wainuiomata", "Same day / next day", "Our home base. No callout surcharge in Wainuiomata.", ["Wainuiomata", "Arakura", "Homedale"]),
    ("Lower Hutt", "Within 24 hours", "Homes, rentals, workshops and offices across the valley floor.", ["Petone", "Gracefield", "Epuni", "Waterloo", "Naenae"]),
    ("Upper Hutt", "Same week", "Regular runs up the valley for homes and businesses.", ["Silverstream", "Trentham", "Upper Hutt Central"]),
    ("Tawa", "24–48 hours", "Heat pump cleans and workplace tagging in the northern suburbs.", ["Tawa", "Linden", "Redwood"]),
    ("Newlands", "Flexible booking", "Booked around your schedule, including Johnsonville.", ["Newlands", "Johnsonville", "Paparangi"]),
    ("Porirua & Greater Wellington", "Scheduled dispatch", "Planned visits across Porirua and the wider region.", ["Porirua", "Wellington City (by arrangement)"]),
]
REVIEWS = [
    ("Craig Henderson", "Workshop Manager · Hutt Valley Engineering", "Test & Tag", "Feb 2026",
     "Midha tested over 350 power tools and industrial units across our facility. The QR tags make tracking effortless, and our audit register was emailed that evening. Punctual, polite, and top-tier Kiwi professionals."),
    ("Sarah McLachlan", "Homeowner · Silverstream, Upper Hutt", "Heat Pump Cleaning", "Jan 2026",
     "Our heat pump smelled musty whenever we turned on heat mode. Midha took the unit apart, treated the coils with foam sanitiser and flushed it thoroughly. The difference in air quality and heating speed was immediate. Highly recommend!"),
    ("Marcus Davies", "Site Foreman · Lower Hutt Construction", "Test & Tag", "Nov 2025",
     "Having a Kiwi technician who understands WorkSafe rules and shows up at 7am before the boys hit the tools is invaluable. Replaced two frayed cords on the spot too."),
    ("Elena Petrov", "Resident · Tawa", "Heat Pump Cleaning", "Oct 2025",
     "Our power bill shot up last winter. Midha cleaned out the caked lint and the leaves in the outdoor coil, and our power use dropped noticeably the next month. Super clean, zero mess left in the living room."),
    ("Kev & Aroha Broughton", "Homeowners · Wainuiomata", "Heat Pump Cleaning", "Sep 2025",
     "Friendly local lads. Gave us honest advice on our heat pump placement and did a great job cleaning both units. Great to support a Kiwi-owned business right here in Wainui."),
    ("Liam O'Connor", "Cafe Owner · Petone", "Test & Tag", "Aug 2025",
     "Tested all our kitchen appliances, coffee grinders and POS gear without disrupting the lunch rush. Clean, quiet, and very reasonably priced. We'll use them every 12 months."),
]
SERVICE_OPTIONS = [
    ("Heat pump – Elite Clean ($129)", "elite"),
    ("Heat pump – Pro Clean ($79)", "pro"),
    ("Heat pump – Comprehensive Clean ($189)", "comprehensive"),
    ("Heat pump – Filter replacement / repairs / pipe insulation", "heat-pump-other"),
    ("Test & Tag (workplace)", "test-tag"),
    ("Medical equipment testing (AS/NZS 3551)", "medical"),
    ("Fire extinguisher & fire blanket checks", "fire"),
    ("Electrical services (lighting, power points, cords)", "electrical"),
    ("Something else", "other"),
]

# Test & tag is offered NZ-wide (heat pump and electrical stay Wellington only).
# Each city page has its own copy so it isn't a "doorway page" with only the name swapped.
RURAL = ("regional-rural-nz", "Regional & rural NZ")
CITIES = [
    dict(slug="auckland", name="Auckland", region="Auckland",
         lead="Testing and tagging to " + STANDARD + " for Auckland construction sites, warehouses, offices and cafés, with QR tags and a digital register.",
         intro=["Auckland has more building sites, hire yards and warehouses than anywhere else in the country, and that gear works hard. Construction and hire equipment is usually tested every 3 months, so a tester who turns up when they say they will matters.",
                "We test across the isthmus and out to the North Shore, West and South Auckland. Large sites can be split over several visits, and early starts mean testing is done before the tools come out."],
         industries=["Construction sites", "Warehouses & logistics", "Hire yards", "Offices", "Cafés & restaurants", "Workshops", "Schools", "Retail"],
         nearby=["Auckland CBD", "North Shore", "Albany", "West Auckland", "East Tāmaki", "Penrose", "Manukau", "Pukekohe"],
         faqs=[("How often should Auckland construction sites test and tag?", "Construction and demolition sites are usually tested every 3 months under AS/NZS 3760, along with RCD checks. We can book your retests in advance so nothing slips."),
               ("Can you test several Auckland sites?", "Yes. Tell us where your sites are and roughly how many items each one has. We’ll quote for them together and keep a separate register for each site.")]),
    dict(slug="hamilton", name="Hamilton", region="Waikato",
         lead="Testing and tagging for Hamilton and Waikato workplaces, from engineering workshops to dairy sheds, done to " + STANDARD + ".",
         intro=["The Waikato runs on agriculture, engineering and manufacturing, and much of that work relies on portable tools, leads and machinery used in tough conditions. Regular testing catches damaged cords and faulty gear before someone gets hurt.",
                "We cover Hamilton city and the surrounding towns, including farms and rural workshops. Tell us how many items you have and where, and you’ll get a fixed price that includes travel."],
         industries=["Engineering workshops", "Manufacturing", "Dairy sheds & farms", "Agricultural contractors", "Offices", "Schools", "Retail", "Cafés"],
         nearby=["Hamilton city", "Cambridge", "Te Awamutu", "Ngāruawāhia", "Huntly", "Morrinsville", "Raglan"],
         faqs=[("Do you test farm and dairy shed equipment?", 'Yes. We test the portable tools, leads and appliances used on farms and in dairy sheds, and flag anything damaged. See our <a href="/test-and-tag/regional-rural-nz/">regional and rural page</a> for how rural visits work.'),
               ("How often should workshop tools be tested?", "Factories, workshops and other heavy-use sites are usually tested every 6 months. Offices and other low-risk areas can go 12 months or longer.")]),
    dict(slug="tauranga", name="Tauranga", region="Bay of Plenty",
         lead="Test and tag for Tauranga and the Western Bay of Plenty: port businesses, packhouses, building sites and offices.",
         intro=["Tauranga is one of the country’s fastest-growing cities, with a busy port, plenty of construction and a large kiwifruit industry around Te Puke. Packhouses and coolstores lean heavily on electrical equipment during the season, so it pays to have everything tested before the rush.",
                "We cover Tauranga, Mount Maunganui, Papamoa and out to Te Puke and Katikati, and can work around early starts and shift patterns."],
         industries=["Packhouses & coolstores", "Orchards", "Port & logistics", "Construction", "Offices", "Hospitality", "Retail", "Schools"],
         nearby=["Tauranga", "Mount Maunganui", "Papamoa", "Bethlehem", "Te Puke", "Ōmokoroa", "Katikati"],
         faqs=[("Can you test our packhouse before the kiwifruit season?", "Yes. Let us know when your season starts and we’ll book testing beforehand, so your gear is tagged and ready when the fruit arrives."),
               ("Do you work around shift times?", "Yes. We can test early in the morning, between shifts or at quieter times so your operation keeps running.")]),
    dict(slug="rotorua", name="Rotorua", region="Bay of Plenty",
         lead="Test and tag for Rotorua hotels, motels, tourism operators, forestry businesses and offices, to " + STANDARD + ".",
         intro=["Rotorua’s hotels, motels and tourism operators have a lot of guest-facing appliances, from kettles and hair dryers to commercial kitchen gear. Forestry and wood processing businesses rely on heavy-duty tools and leads.",
                "We plan testing around your guests and your busy times, so rooms and kitchens stay open while we work."],
         industries=["Hotels & motels", "Tourism operators", "Forestry & wood processing", "Cafés & restaurants", "Offices", "Schools"],
         nearby=["Rotorua central", "Ngongotahā", "Fairy Springs", "Lynmore", "Owhata", "Reporoa (by arrangement)"],
         faqs=[("Can you test appliances in guest rooms?", "Yes. We test kettles, irons, hair dryers, TVs and other room appliances, working floor by floor around housekeeping so rooms aren’t held up."),
               ("Do you test forestry and sawmill equipment?", "We test portable electrical tools, leads and appliances to " + STANDARD + ". Tell us what’s on site and we’ll confirm what we can test.")]),
    dict(slug="whangarei", name="Whangārei", region="Northland",
         lead="Test and tag across Whangārei and Northland for marine businesses, workshops, building sites and offices.",
         intro=["From boat builders and marine engineers around the harbour to building sites and offices in town, Whangārei businesses use plenty of portable electrical gear, often in damp, salty conditions that are hard on cords and plugs.",
                "We cover Whangārei and nearby towns, and further into Northland by arrangement. Your quote includes travel, so the price is clear from the start."],
         industries=["Marine & boat building", "Engineering workshops", "Construction", "Healthcare", "Schools", "Offices", "Retail", "Hospitality"],
         nearby=["Whangārei city", "Kamo", "Tikipunga", "Onerahi", "Hikurangi", "Ruakākā", "Kerikeri (by arrangement)"],
         faqs=[("Does salt air affect electrical equipment?", "It can. Moisture and salt speed up corrosion on plugs, sockets and leads, so equipment used around boats and the coast benefits from regular inspection and testing."),
               ("Do you cover the rest of Northland?", 'Yes, by arrangement. See our <a href="/test-and-tag/regional-rural-nz/">regional and rural page</a> and tell us where you are.')]),
    dict(slug="napier-hastings", name="Napier & Hastings", region="Hawke’s Bay",
         lead="Test and tag for Napier, Hastings and Hawke’s Bay orchards, packhouses, wineries, food processors and offices.",
         intro=["Hawke’s Bay is fruit, wine and food country. Orchards, packhouses, wineries and processing plants all rely on electrical equipment, alongside Napier Port and a busy construction scene. Seasonal sites benefit from getting everything tested before harvest.",
                "We cover Napier, Hastings, Havelock North and the surrounding area, with QR tags and a digital register for every site."],
         industries=["Orchards & packhouses", "Wineries", "Food processing", "Port & logistics", "Construction", "Offices", "Schools", "Hospitality"],
         nearby=["Napier", "Ahuriri", "Taradale", "Hastings", "Havelock North", "Flaxmere", "Clive"],
         faqs=[("Can you test before harvest or vintage?", "Yes. Tell us when your season starts and we’ll book testing before then, so seasonal staff start with safe, tagged equipment."),
               ("Do you test kitchen and bar equipment at wineries?", "Yes. Cellar door kitchens, bars and function areas can be tested along with the winery’s tools and leads.")]),
    dict(slug="new-plymouth", name="New Plymouth", region="Taranaki",
         lead="Test and tag for New Plymouth and Taranaki engineering firms, energy contractors, dairy businesses and offices.",
         intro=["Taranaki has a strong engineering and energy sector, alongside dairy farming and manufacturing. Workshops and contractors often use heavy-duty tools and long extension leads that need regular checking.",
                "We cover New Plymouth, Bell Block, Waitara and Inglewood, and further around the mountain by arrangement."],
         industries=["Engineering", "Energy contractors", "Manufacturing", "Dairy & farms", "Construction", "Offices", "Schools", "Retail"],
         nearby=["New Plymouth", "Bell Block", "Waitara", "Inglewood", "Ōakura", "Stratford (by arrangement)"],
         faqs=[("Can you test contractors’ tools before a site induction?", "Yes. Many sites ask contractors to show that their tools and leads carry current tags. We can test a contractor’s kit so it’s ready to go."),
               ("How do I know when items are due for a retest?", "Each item has a QR tag showing when it was tested and when the next test is due, and we send reminders before your retests.")]),
    dict(slug="palmerston-north", name="Palmerston North", region="Manawatū",
         lead="Test and tag for Palmerston North and Manawatū warehouses, distribution centres, schools, healthcare and offices.",
         intro=["Palmerston North is a major distribution hub for the lower North Island, with large warehouses and freight operations alongside a big education and healthcare sector. Busy sites like these need testing that fits around shifts and deliveries.",
                "We cover Palmerston North city, Feilding, Ashhurst and the wider Manawatū."],
         industries=["Warehouses & distribution", "Freight & logistics", "Education", "Healthcare", "Offices", "Retail", "Agriculture", "Hospitality"],
         nearby=["Palmerston North", "Feilding", "Ashhurst", "Bunnythorpe", "Longburn", "Levin (by arrangement)"],
         faqs=[("Can you test a large warehouse without stopping work?", "Yes. We work section by section and around your shifts, so the warehouse keeps moving while we test."),
               ("Can you test schools during the holidays?", "Yes. We can test classroom appliances, computers and leads during school holidays or after hours, so lessons aren’t interrupted.")]),
    dict(slug="whanganui", name="Whanganui", region="Manawatū-Whanganui",
         lead="Test and tag for Whanganui manufacturers, workshops, studios, schools, healthcare providers and small businesses.",
         intro=["Whanganui has a strong mix of manufacturing, workshops, schools and healthcare, plus a creative community of studios and makers. Whatever the size of your business, regular testing helps keep your team and visitors safe.",
                "We cover Whanganui city and the surrounding district."],
         industries=["Manufacturing", "Workshops", "Studios & makers", "Healthcare", "Schools", "Offices", "Retail", "Hospitality"],
         nearby=["Whanganui central", "Castlecliff", "Aramoho", "Gonville", "Springvale", "Marton (by arrangement)"],
         faqs=[("Do small businesses need test and tag?", "Every business must keep its electrical equipment safe. Test and tag is the most common way to show you’re doing that, whether you have 10 items or 1,000."),
               ("What happens if an item fails?", "It’s tagged out of service straight away so nobody uses it, and it’s listed in your register so you know what needs repairing or replacing.")]),
    dict(slug="wellington", name="Wellington", region="Wellington",
         lead="Test and tag across Wellington, the Hutt Valley, Porirua and Kāpiti, from our home base in Wainuiomata.",
         intro=["Wellington is home. We’re based in Wainuiomata, so Wellington workplaces get our quickest bookings, whether that’s a government office, a café on Cuba Street or a workshop in Seaview.",
                "We test for offices, construction sites, workshops, schools and hospitality across the region, and in Wellington we can also look after your heat pumps and electrical work while we’re there."],
         industries=["Offices", "Construction sites", "Workshops", "Cafés & bars", "Schools", "Retail", "Rental properties", "Community halls"],
         nearby=["Wellington CBD", "Lower Hutt", "Petone", "Seaview & Gracefield", "Wainuiomata", "Upper Hutt", "Porirua", "Tawa", "Johnsonville", "Kāpiti Coast"],
         faqs=[("How quickly can you test in Wellington?", "Wellington is our home region, so it gets our fastest bookings. Wainuiomata and Hutt Valley jobs can often be booked within a day or two."),
               ("Can you clean our heat pumps in the same visit?", 'Yes. In the Wellington region we also do <a href="/heat-pump-cleaning/">heat pump cleaning</a> and <a href="/electrical-services/">electrical work</a>, so one visit can cover everything.')]),
    dict(slug="nelson", name="Nelson", region="Nelson Tasman",
         lead="Test and tag for Nelson and Tasman seafood processors, orchards, workshops, hospitality and offices.",
         intro=["Nelson’s economy is built on seafood, horticulture, forestry and tourism. Processing plants, coolstores and busy hospitality kitchens all depend on equipment that needs regular checking.",
                "We cover Nelson, Stoke and Richmond, and out to Māpua and Motueka."],
         industries=["Seafood processing", "Orchards & horticulture", "Forestry", "Hospitality", "Construction", "Offices", "Schools", "Retail"],
         nearby=["Nelson", "Tāhunanui", "Stoke", "Richmond", "Brightwater", "Māpua", "Motueka"],
         faqs=[("Do you test equipment used in wet or cold areas?", "Yes. Wet areas, coolstores and processing rooms are hard on cords and plugs, so we inspect that equipment closely and recommend a suitable retest interval."),
               ("Can you test our café or restaurant kitchen?", "Yes. We test plug-in kitchen appliances, coffee grinders and POS gear around your service times.")]),
    dict(slug="blenheim", name="Blenheim", region="Marlborough",
         lead="Test and tag for Blenheim and Marlborough vineyards, wineries, contractors, Picton businesses and offices.",
         intro=["Marlborough is New Zealand’s biggest wine region. Vineyards, wineries and their contractors use a lot of plug-in gear, from chargers for electric pruning tools to winery equipment. Picton adds port, ferry and tourism businesses to the mix.",
                "We cover Blenheim, Renwick, Picton and the surrounding district."],
         industries=["Vineyards", "Wineries", "Vineyard contractors", "Port & tourism", "Hospitality", "Offices", "Schools", "Retail"],
         nearby=["Blenheim", "Renwick", "Spring Creek", "Picton", "Seddon", "Havelock (by arrangement)"],
         faqs=[("Can you test chargers for electric pruning tools?", "Yes. Plug-in chargers, leads and power tools are all tested and tagged, and it’s worth doing before pruning season starts."),
               ("Can our contractors’ gear be tested too?", "Yes. We can test your contractors’ tools and leads so everything used on your vineyard is tagged.")]),
    dict(slug="christchurch", name="Christchurch", region="Canterbury",
         lead="Test and tag for Christchurch and Canterbury building sites, manufacturers, warehouses, schools and offices.",
         intro=["Christchurch has one of the country’s busiest construction scenes, plus a large manufacturing and warehousing base around Hornby, Sockburn and Islington. Building sites and hire equipment are usually tested every 3 months.",
                "We cover the city and Lyttelton, plus the growing towns of Rolleston, Lincoln, Rangiora and Kaiapoi."],
         industries=["Construction sites", "Manufacturing", "Warehouses", "Hire equipment", "Schools & tertiary", "Offices", "Hospitality", "Retail"],
         nearby=["Christchurch central", "Riccarton", "Hornby", "Papanui", "Lyttelton", "Rolleston", "Lincoln", "Rangiora", "Kaiapoi"],
         faqs=[("Do you test hire equipment?", "Yes. Hire equipment is usually tested every 3 months, with a visual check before each hire. We can set up a regular schedule for your fleet."),
               ("Can you tag our equipment before we open?", "Yes. We can check and tag your equipment before opening day, so your register is complete from the start.")]),
    dict(slug="dunedin", name="Dunedin", region="Otago",
         lead="Test and tag for Dunedin and Otago tertiary providers, student accommodation, healthcare, hospitality and offices.",
         intro=["Dunedin is a university city, with a large student population, big tertiary and healthcare sectors, and plenty of cafés and bars. Halls, flats and shared kitchens see a lot of appliances come and go, which makes regular testing worthwhile.",
                "We cover the city, Mosgiel and Port Chalmers, and the wider Otago coast by arrangement."],
         industries=["Tertiary & education", "Student accommodation", "Healthcare", "Hospitality", "Port & logistics", "Manufacturing", "Offices", "Retail"],
         nearby=["Dunedin central", "North Dunedin", "South Dunedin", "Green Island", "Mosgiel", "Port Chalmers", "Waikouaiti (by arrangement)"],
         faqs=[("Can you test appliances in student accommodation?", "Yes. We test shared kitchen appliances, heaters and other plug-in items, and can work during semester breaks to avoid disruption."),
               ("How do you handle items that fail?", "Anything that fails is tagged out of service straight away and listed in your register, so you know exactly what needs repairing or replacing.")]),
    dict(slug="queenstown", name="Queenstown", region="Otago",
         lead="Test and tag for Queenstown hotels, restaurants, tourism operators, ski businesses and building sites.",
         intro=["Queenstown runs on tourism and hospitality, with hotels, restaurants, bars and adventure operators working flat out through the seasons, plus a steady flow of construction. Equipment gets heavy use, so regular testing matters.",
                "We plan visits for quieter times, such as the shoulder seasons, so testing doesn’t get in the way of your busiest weeks. We cover Queenstown, Frankton, Arrowtown and Cromwell, and Wānaka by arrangement."],
         industries=["Hotels & lodges", "Restaurants & bars", "Tourism operators", "Ski & snow businesses", "Construction", "Holiday rentals", "Offices", "Retail"],
         nearby=["Queenstown central", "Frankton", "Kelvin Heights", "Jacks Point", "Arrowtown", "Cromwell", "Wānaka (by arrangement)"],
         faqs=[("Can you test before the ski season?", "Yes. Getting rental, workshop and café equipment tested before the season starts means you’re ready for the first busy weekend."),
               ("Do you test appliances in holiday rentals?", "Yes. Appliances in holiday homes and serviced apartments can be tested and tagged between guest stays.")]),
    dict(slug="invercargill", name="Invercargill", region="Southland",
         lead="Test and tag for Invercargill and Southland dairy, meat processing, engineering, port and farm businesses.",
         intro=["Southland is farming country, with dairy and sheep farms, meat and dairy processing, and the engineering firms that keep it all running. Bluff adds port and seafood businesses. These are demanding environments for cords, leads and tools.",
                "We cover Invercargill, Bluff, Gore and Winton, and rural Southland by arrangement."],
         industries=["Dairy & meat processing", "Farms", "Engineering", "Port & seafood", "Construction", "Offices", "Schools", "Retail"],
         nearby=["Invercargill", "Otatara", "Bluff", "Winton", "Riverton", "Gore", "Mataura"],
         faqs=[("Do you test equipment on farms?", 'Yes. See our <a href="/test-and-tag/regional-rural-nz/">regional and rural page</a> for how we plan visits to farms and rural sites.'),
               ("How often should processing plant equipment be tested?", "Harsh environments like processing plants and factories are usually tested every 6 months. We’ll recommend the right interval for each area of your site.")]),
]
NZ_REGIONS = ["Northland", "Auckland", "Waikato", "Bay of Plenty", "Gisborne", "Hawke’s Bay", "Taranaki", "Manawatū-Whanganui",
              "Wellington", "Tasman", "Nelson", "Marlborough", "West Coast", "Canterbury", "Otago", "Southland"]

# ---------------------------------------------------------------- layout
def head(title, desc, path, extra_ld=None):
    url = SITE + path
    ld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": SITE + "/#business",
        "name": "Midha Limited", "url": SITE + "/", "telephone": TEL, "email": EMAIL,
        "image": SITE + "/assets/img/og-image.jpg", "logo": SITE + "/assets/img/logo-512.png",
        "description": "Test & tag, medical equipment testing and fire extinguisher checks across New Zealand, plus heat pump cleaning and electrical services in Greater Wellington.",
        "address": {"@type": "PostalAddress", "addressLocality": "Wainuiomata", "addressRegion": "Wellington", "addressCountry": "NZ"},
        "areaServed": [{"@type": "Country", "name": "New Zealand"}, {"@type": "AdministrativeArea", "name": "Wellington Region"}],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:30", "closes": "18:00"}],
    }]
    if extra_ld: ld += extra_ld
    return f"""<!doctype html>
<html lang="en-NZ" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#FDFCF8">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Midha Limited">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_NZ">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=general-sans@600,700&amp;f[]=switzer@400,500,600&amp;display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">
<script src="/assets/js/main.js?v=20261021" defer></script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0], ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

def nav(active):
    def cur(p): return ' aria-current="page"' if active == p else ""
    menu = []
    for _, href, name, ic in SERVICES:
        menu.append((href, name, ic))
        if href == "/test-and-tag/":
            menu += [(MED_PATH, "Medical equipment testing", "cross"), (FIRE_PATH, "Fire extinguisher checks", "flame")]
    services = "".join(f'<li><a href="{href}"{cur(href)}>{icon(ic, 18)} {e(name)}</a></li>' for href, name, ic in menu)
    areas = (f'<li><a href="/test-and-tag/#locations">{icon("tag", 18)} Test &amp; tag: all of NZ</a></li>'
             f'<li><a href="/service-areas/">{icon("pin", 18)} Heat pumps &amp; electrical: Wellington</a></li>')
    return f"""<div class="announce" role="region" aria-label="Promotion">Win a free heat pump clean, worth $79. A new Wellington winner every 3 months. <a href="/heat-pump-cleaning/#giveaway">How to enter</a></div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Midha Limited, home">
      <img src="/assets/img/logo-96.png" width="48" height="48" alt="">
      <span class="brand-name"><strong>Midha Limited</strong><span>Test &amp; tag · Heat pumps · Electrical</span></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
        <li class="has-sub"><button class="nav-parent" type="button" aria-expanded="false" aria-controls="sub-services">Services {icon("chev", 16)}</button>
          <ul class="submenu" id="sub-services">{services}</ul></li>
        <li class="has-sub"><button class="nav-parent" type="button" aria-expanded="false" aria-controls="sub-areas">Service areas {icon("chev", 16)}</button>
          <ul class="submenu" id="sub-areas">{areas}</ul></li>
        <li><a href="/reviews/"{cur("/reviews/")}>Reviews</a></li>
        <li><a href="/about/"{cur("/about/")}>About</a></li>
        <li><a href="/contact/"{cur("/contact/")}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{TEL}">{PHONE}</a>
      <a class="btn btn--primary" href="/contact/#quote">Get a quote</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{icon("menu", 22)}</button>
    </div>
  </div>
</header>
"""

def footer():
    services = "".join(f'<li><a href="{h}">{e(n)}</a></li>' for _, h, n, _ in SERVICES)
    services = services.replace('Test &amp; Tag</a></li>', f'Test &amp; Tag</a></li><li><a href="{MED_PATH}">Medical equipment testing</a></li><li><a href="{FIRE_PATH}">Fire extinguisher checks</a></li>', 1)
    top =["auckland", "hamilton", "tauranga", "wellington", "christchurch", "dunedin"]
    areas = "".join(f'<li><a href="/test-and-tag/{c["slug"]}/">Test &amp; tag {e(c["name"])}</a></li>' for c in CITIES if c["slug"] in top)
    return f"""<footer class="site-footer on-dark">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/"><img src="/assets/img/logo-96.png" width="48" height="48" alt=""><span class="brand-name"><strong>Midha Limited</strong></span></a>
        <p>Test &amp; tag, medical equipment testing and fire extinguisher checks for workplaces across New Zealand. Heat pump cleaning and electrical services for homes and businesses in Greater Wellington. Based in Wainuiomata.</p>
        <p class="footer-small">100% NZ owned &amp; operated · {EST}</p>
      </div>
      <div><h2>Services</h2><ul>{services}<li><a href="/heat-pump-cleaning/#healthy-homes">Healthy Homes heating</a></li><li><a href="/service-areas/">Wellington service areas</a></li></ul></div>
      <div><h2>Test &amp; tag NZ</h2><ul>{areas}<li><a href="/test-and-tag/#locations">All locations</a></li></ul></div>
      <div><h2>Get in touch</h2><ul>
        <li><a href="tel:{TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{HOURS}</li>
        <li>Wainuiomata, Wellington</li>
        <li><a href="/contact/#quote">Request a quote</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> Midha Limited. All rights reserved.</span>
      <span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/giveaway-terms/">Giveaway terms</a> · <a href="/about/">About</a> · <a href="/contact/">Contact</a></span>
    </div>
  </div>
</footer>
<div class="action-bar" role="region" aria-label="Quick contact">
  <a class="call" href="tel:{TEL}">Call now</a>
  <a class="quote-btn" href="/contact/#quote">Get a quote</a>
</div>
</body>
</html>
"""

def slug(s):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-").replace("--", "-").replace("--", "-")

def breadcrumbs(items):
    lis = "".join(
        (f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>') for n, h in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + h} if h else {})} for i, (n, h) in enumerate(items)]}
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld

def page_hero(crumbs, eyebrow, h1, lead, ctas=True, badge=""):
    bc, ld = breadcrumbs(crumbs)
    btns = f"""<div class="btn-row"><a class="btn btn--primary" href="/contact/#quote">Get a free quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>""" if ctas else ""
    return f"""<section class="page-hero"><div class="wrap">{bc}
  <div class="hero-meta">{badge}<span class="eyebrow">{eyebrow}</span></div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>{btns}
</div></section>""", ld

def quote_section(heading="Get a fixed-price quote", sub="Tell us what you need and we’ll reply within 2 hours during business hours.", sage=False, default=""):
    opts = "".join(f'<option value="{v}"{" selected" if v == default else ""}>{e(l)}</option>' for l, v in SERVICE_OPTIONS)
    return f"""<section class="section{' section--sage' if sage else ''}" id="quote" aria-labelledby="quote-title">
<div class="wrap quote">
  <div class="quote-info reveal">
    <span class="eyebrow">Free quote · no obligation</span>
    <h2 id="quote-title">{heading}</h2>
    <p class="lead">{sub}</p>
    <ul class="contact-list">
      <li>{icon("phone")}<span><a href="tel:{TEL}">{PHONE}</a><br><span class="note">Call or text</span></span></li>
      <li>{icon("mail")}<span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
      <li>{icon("clock")}<span>{HOURS}<br><span class="note">Urgent callouts available</span></span></li>
      <li>{icon("pin")}<span>Based in Wainuiomata<br><span class="note">Test &amp; tag, medical &amp; fire checks NZ-wide · heat pumps &amp; electrical in Greater Wellington</span></span></li>
    </ul>
  </div>
  <div class="form-card reveal">
    <form class="quote-form" novalidate>
      <div class="form-grid">
        <div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name"></div>
        <div class="field"><label for="phone">Phone number <span aria-hidden="true">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" required aria-describedby="phone-err"><span class="error" id="phone-err">Please enter a phone number so we can reach you.</span></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="email-err"><span class="error" id="email-err">That email doesn’t look right.</span></div>
        <div class="field"><label for="suburb">Suburb or town</label><input id="suburb" name="suburb" autocomplete="address-level2"></div>
        <div class="field full"><label for="service">What do you need? <span aria-hidden="true">*</span></label><select id="service" name="service" required aria-describedby="service-err"><option value="">Choose a service</option>{opts}</select><span class="error" id="service-err">Please choose a service.</span></div>
        <div class="field full"><label for="details">Job details <span class="hint">(optional: number of heat pumps, items or extinguishers, timing)</span></label><textarea id="details" name="details"></textarea></div>
        <div class="hp-field" aria-hidden="true"><label for="_gotcha">Leave this empty</label><input id="_gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
        <div class="full"><button class="btn btn--primary btn--block" type="submit">Send my request</button></div>
      </div>
      <div class="form-status" role="status" aria-live="polite"></div>
      <ul class="seals"><li><span class="tick">✓</span>Fixed price</li><li><span class="tick">✓</span>No obligation</li><li><span class="tick">✓</span>Your details stay private</li></ul>
      <p class="form-note">* Required. We only use your details to reply to you and do your job. See our <a href="/privacy/">privacy policy</a>.</p>
    </form>
  </div>
</div></section>"""

def faq(items, title="Common questions", sage=False, eyebrow="FAQ"):
    body = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a.replace("<a ", "<a ")).replace("&amp;", "&")}} for q, a in items]}
    return f"""<section class="section{' section--sage' if sage else ''}" aria-labelledby="faq-title"><div class="wrap">
<div class="section-head"><span class="eyebrow">{eyebrow}</span><h2 id="faq-title">{title}</h2></div>
<div class="faq">{body}</div></div></section>""", ld

def review_card(r):
    name, who, svc, date, text = r
    return f"""<article class="card review reveal">
  <div class="stars" role="img" aria-label="5 out of 5 stars">★★★★★</div>
  <blockquote><p>“{e(text)}”</p></blockquote>
  <div class="meta"><p class="who"><strong>{e(name)}</strong><br>{e(who)}</p><span class="badge badge--soft">{e(svc)}</span></div>
  <p class="note">{e(date)}</p>
</article>"""

def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

TAG_SVG = """<svg viewBox="0 0 220 300" role="img" aria-label="Illustration of a test tag reading Tested, Passed">
<rect x="20" y="20" width="180" height="260" rx="24" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="4"/>
<circle cx="110" cy="58" r="14" fill="#E2E8E4" stroke="#1C1C1C" stroke-width="4"/>
<text x="110" y="118" text-anchor="middle" font-family="General Sans, sans-serif" font-weight="700" font-size="26" fill="#1C1C1C">TESTED</text>
<text x="110" y="150" text-anchor="middle" font-family="Switzer, sans-serif" font-weight="600" font-size="16" fill="#6E6354">AS/NZS 3760</text>
<line x1="44" y1="176" x2="176" y2="176" stroke="#978B7A" stroke-width="3" stroke-dasharray="8 6"/>
<rect x="44" y="194" width="58" height="58" rx="6" fill="none" stroke="#1C1C1C" stroke-width="4"/>
<rect x="56" y="206" width="14" height="14" fill="#1C1C1C"/><rect x="76" y="226" width="14" height="14" fill="#1C1C1C"/><rect x="56" y="230" width="10" height="10" fill="#1C1C1C"/>
<text x="118" y="214" font-family="Switzer, sans-serif" font-weight="600" font-size="14" fill="#1C1C1C">PASSED</text>
<text x="118" y="238" font-family="Switzer, sans-serif" font-size="13" fill="#4A4A45">Retest due</text>
</svg>"""

BULB_SVG = """<svg viewBox="0 0 220 220" role="img" aria-label="Illustration of a ceiling downlight">
<rect x="20" y="30" width="180" height="16" rx="8" fill="#1C1C1C"/>
<path d="M70 46h80l-10 34H80Z" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="4"/>
<path d="M60 92 30 190M110 92v100M160 92l30 98" stroke="#978B7A" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 12"/>
<ellipse cx="110" cy="84" rx="30" ry="6" fill="#D4AF37"/>
</svg>"""

# ---------------------------------------------------------------- pages
pages = []

def home():
    hero_img = pic("indoor-coil-clean", "Midha technician washing the coil of an indoor heat pump in a Wellington home", big=True, eager=True, sizes="100vw")
    chooser = f"""
<div class="wrap"><div class="chooser">
  <a class="card card--lift" href="/test-and-tag/">
    <div class="icon-chip">{icon("tag", 26)}</div><span class="num">For workplaces · NZ-wide</span>
    <h2 class="h3" style="font-size:var(--fs-h3)">Test &amp; Tag</h2>
    <p>{STANDARD} testing for tools, appliances, leads and RCDs anywhere in New Zealand, with QR tags and a digital register. Medical equipment and fire extinguisher checks too.</p>
    <span class="more">Test &amp; tag details →</span></a>
  <a class="card card--lift card--ink on-dark" href="/heat-pump-cleaning/">
    <div class="icon-chip">{icon("fan", 26, "#FFFFFF")}</div><span class="num" style="color:#C9BFAE">For homes &amp; rentals · Wellington</span>
    <h2 style="font-size:var(--fs-h3)">Heat Pump Cleaning</h2>
    <p>Deep cleans from <strong style="color:#fff">$79 per unit</strong>, GST incl. Mould gone, airflow back, lower power bills.</p>
    <span class="more" style="color:#C9BFAE">See packages &amp; prices →</span></a>
  <a class="card card--lift" href="/electrical-services/">
    <div class="icon-chip">{icon("bulb", 26)}</div><span class="num">For homes &amp; businesses · Wellington</span>
    <h2 style="font-size:var(--fs-h3)">Electrical Services</h2>
    <p>Light installations, LED downlights, security and sensor lights, power points, cord and lead repairs.</p>
    <span class="more">Electrical details →</span></a>
</div></div>"""
    stats = """
<div class="wrap"><div class="stats" aria-label="Midha in numbers">
  <div class="stat"><strong>14,500+</strong><span>items tested &amp; tagged for businesses</span></div>
  <div class="stat"><strong>200+</strong><span>home heat pumps serviced</span></div>
  <div class="stat"><strong>&lt; 2 hrs</strong><span>average quote reply</span></div>
  <div class="stat"><strong>5.0 <span class="star" aria-hidden="true">★</span></strong><span>Google rating</span></div>
</div></div>"""
    packages = packages_section(compact=True)
    why = f"""
<section class="section section--ink on-dark" aria-labelledby="why-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Why Midha</span><h2 id="why-title">Local, upfront and properly done.</h2>
  <p style="color:#D9D6CE">We take the hassle out of compliance and heat pump care, whether you run a busy workshop or a family home.</p></div>
  <div class="feature-list">
    <div class="feature reveal"><div class="icon-chip">{icon("dollar", 24, "#FFFFFF")}</div><div><h3>Fixed, upfront pricing</h3><p>The price on your quote is the price you pay. No surprise travel or admin fees.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("qr", 24, "#FFFFFF")}</div><div><h3>Digital QR reports</h3><p>Every tagged item gets a QR code, and your register arrives as a PDF with reminders before retests are due.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("leaf", 24, "#FFFFFF")}</div><div><h3>A real deep clean</h3><p>Not just a filter wipe. We wash the coils and fan to clear mould and bacteria from the air you breathe.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("pin", 24, "#FFFFFF")}</div><div><h3>Wellington-based, NZ-wide</h3><p>Prompt heat pump and electrical callouts across the Hutt Valley, northern suburbs and Porirua, and test &amp; tag anywhere in New Zealand.</p></div></div>
  </div>
  <div class="btn-row" style="margin-top:36px"><a class="btn btn--gold" href="/about/">About Midha</a></div>
</div></section>"""
    reviews = "".join(review_card(r) for r in REVIEWS[:3])
    rev = f"""
<section class="section" aria-labelledby="rev-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">5.0 on Google</span><h2 id="rev-title">Trusted by homes and workplaces across Wellington.</h2></div>
  <div class="grid grid-3">{reviews}</div>
  <div class="btn-row" style="margin-top:28px"><a class="btn btn--outline" href="/reviews/">Read all reviews</a></div>
</div></section>"""
    area_sec = f"""
<section class="section section--sage" aria-labelledby="areas-title"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Where we work</span><h2 id="areas-title">Test &amp; tag NZ-wide. Heat pumps and electrical in Wellington.</h2>
  <p class="lead">We test and tag workplaces from Whangārei to Invercargill. Heat pump cleaning and electrical work are for homes and businesses across Greater Wellington, from our base in Wainuiomata.</p>
  <div class="btn-row"><a class="btn btn--primary" href="/test-and-tag/#locations">Test &amp; tag locations</a><a class="btn btn--light" href="/service-areas/">Wellington service areas</a></div></div>
  <div class="reveal">{location_links()}</div>
</div></section>"""
    fq, fld = faq([
        ("How much does a heat pump clean cost?", 'Our Pro Clean is $79, Elite Clean $129 and Comprehensive Clean $189. Prices are per heat pump and include GST. <a href="/heat-pump-cleaning/">Compare packages</a>.'),
        ("Do you only do test &amp; tag for businesses?".replace("&amp;", "&"), "Test &amp; tag is mainly for workplaces, construction sites, schools, cafés and offices, but we’re happy to test gear for anyone who needs it."),
        ("Do you test medical equipment and fire extinguishers?", f'Yes, anywhere in New Zealand. We test medical equipment such as beds, hoists and pumps to {MED_STD}, and check fire extinguishers and fire blankets to {FIRE_STD}, often in the same visit as your test &amp; tag. See <a href="{MED_PATH}">medical equipment testing</a> and <a href="{FIRE_PATH}">fire extinguisher checks</a>.'),
        ("How quickly can you come out?", "We aim to reply to every quote request within 2 hours during business hours. Wainuiomata jobs can often be booked same day or next day; see our service areas for other suburbs."),
        ("Which areas do you cover?", 'Test &amp; tag is available right across New Zealand. <a href="/test-and-tag/#locations">See test &amp; tag locations</a>. Heat pump cleaning and electrical work cover Wainuiomata, Lower Hutt, Upper Hutt, Tawa, Newlands, Porirua and the wider Wellington region. <a href="/service-areas/">See Wellington service areas</a>.'),
    ], title="Got questions?")
    ld = [fld]
    body = f"""<main id="main">
<section class="hero"><div class="wrap"><div class="hero-frame">
  {hero_img}
  <div class="hero-panel glass reveal">
    <div class="hero-meta"><span class="badge badge--urgent">Win a free heat pump clean</span><span>Wainuiomata-based · 100% NZ owned</span></div>
    <h1>Test &amp; tag, heat pump cleaning and electrical work, sorted.</h1>
    <p class="lead">Test &amp; tag for workplaces anywhere in New Zealand, plus heat pump cleaning and electrical work for Greater Wellington. Fixed upfront prices, digital reports, and a reply within 2 hours.</p>
    <div class="btn-row"><a class="btn btn--primary" href="/contact/#quote">Get a free quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
</div></div></section>
<h2 class="visually-hidden">Our three services</h2>
{chooser}
{stats}
{packages}
{why}
{rev}
{area_sec}
{fq}
{quote_section()}
</main>"""
    write("/", head("Test & Tag NZ-wide | Heat Pump Cleaning Wellington | Midha",
                    "AS/NZS 3760:2022 test & tag for workplaces across New Zealand. Heat pump cleaning from $79 and electrical services in Lower Hutt, Upper Hutt and Wellington.",
                    "/", ld) + nav("/") + body + footer())

def packages_section(compact=False):
    pro_in = """<h4>Indoor unit cleaning</h4><ul><li>Vacuum clean and disinfect filters, housing and cover</li><li>Coil clean treatment and disinfection of evaporator coils</li><li>Clean condensate tray, fan and thermostat</li><li>Advice on any mould found</li></ul>
<h4>Indoor unit checks</h4><ul><li>Inspect evaporator coil for leaks and tighten electrical connections</li><li>Operational and temperature checks</li><li>Assess filters and unit for damage</li><li>Check fan speed and remote settings</li><li>Noise and vibration checks</li></ul>
<h4>Outdoor unit cleaning</h4><ul><li>Coil clean treatment and pressure wash of condenser coils</li><li>Clean condenser housing and fan</li><li>Remove debris and blockages</li></ul>
<h4>Outdoor unit checks</h4><ul><li>Inspect for damage, oil leaks and rodents</li><li>Check drain is flowing and connections are secure</li><li>Condenser safety and mounting stability</li><li>Inspect pipe insulation and check for corrosion</li><li>Noise and vibration assessment</li></ul>"""
    elite_in = """<ul><li>Everything in Pro Clean</li><li>Full pressure wash of the indoor unit to remove all contaminants</li><li>Full pressure wash of the outdoor unit</li><li>Completed maintenance check sheet for your records</li></ul>"""
    comp_in = """<ul><li>Everything in Elite Clean</li><li>Remove and clean the evaporator housing and cover</li><li>Pressure wash the blower fan and air well</li><li>Anti-mould treatment on filters, evaporator coils and condensate tray</li><li>Clean and sanitise all housing and cover parts</li><li>3-month mould-free guarantee: if mould comes back, we re-clean free</li></ul>"""
    det = lambda inner: "" if compact else f'<details class="inclusions"><summary>Everything included</summary>{inner}</details>'
    return f"""
<section class="section section--sage" id="packages" aria-labelledby="pk-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Heat pump cleaning · prices per unit, GST incl.</span><h2 id="pk-title">Pick the clean your heat pump needs.</h2>
  <p>Every package includes a full set of indoor and outdoor safety checks. Got two heat pumps? Simply multiply by two.</p></div>
  <div class="grid grid-3 price-grid">
    <article class="card card--lift price-card reveal">
      <div class="head"><h3>Pro Clean</h3></div>
      <div class="price">$79 <small>per unit</small></div>
      <ul class="check-list"><li>Indoor unit vacuum clean and disinfect</li><li>Outdoor unit pressure wash</li><li>Full indoor and outdoor checks</li></ul>
      {det(pro_in)}
      <a class="btn btn--outline" href="/contact/?service=pro#quote" data-service="pro">Book Pro Clean</a>
    </article>
    <article class="card card--lift card--ink price-card on-dark reveal">
      <div class="head"><h3>Elite Clean</h3><span class="badge badge--gold">Most popular</span></div>
      <div class="price">$129 <small>per unit</small></div>
      <ul class="check-list"><li>Everything in Pro Clean</li><li>Indoor <em>and</em> outdoor units pressure washed</li><li>Completed maintenance check sheet</li></ul>
      {det(elite_in)}
      <a class="btn btn--gold" href="/contact/?service=elite#quote" data-service="elite">Book Elite Clean</a>
    </article>
    <article class="card card--lift price-card reveal">
      <div class="head"><h3>Comprehensive Clean</h3></div>
      <div class="price">$189 <small>per unit</small></div>
      <ul class="check-list"><li>Everything in Elite Clean</li><li>Housing, cover and blower fan deep clean</li><li>Anti-mould treatment with a 3-month mould-free guarantee</li></ul>
      {det(comp_in)}
      <a class="btn btn--outline" href="/contact/?service=comprehensive#quote" data-service="comprehensive">Book Comprehensive</a>
    </article>
  </div>
  {'<div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="/heat-pump-cleaning/">See full heat pump details</a></div>' if compact else ''}
</div></section>"""

def heat_pump():
    hero, bld = page_hero([("Home", "/"), ("Heat Pump Cleaning", None)],
        "Heat pump cleaning · Greater Wellington", "Heat pump cleaning that clears the mould and cuts the power bill.",
        "Pro, Elite and Comprehensive cleans from $79 per unit, GST included. Plus filter replacement, emergency repairs, pipe insulation repair and Healthy Homes heating checks.")
    extras = f"""
<section class="section" aria-labelledby="extra-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Also available · quote on request</span><h2 id="extra-title">Repairs, filters and compliance.</h2></div>
  <div class="grid grid-2">
    <article class="card reveal" id="filter-replacement"><div class="icon-chip">{icon("fan")}</div><h3>Filter replacement</h3><p>Worn or damaged filters let dust straight through. We replace them so your heat pump keeps delivering clean, healthy air.</p></article>
    <article class="card reveal" id="emergency-repairs"><div class="icon-chip">{icon("wrench")}</div><h3>Emergency repairs</h3><p>Heat pump stopped working, blowing cold or making strange noises? Call us for a prompt visit to diagnose the problem and get it running again.</p></article>
    <article class="card card--media reveal" id="pipe-insulation">
      <div class="before-after" style="padding:16px 16px 0">
        <figure>{pic("pipe-insulation-before", "Split and weathered heat pump pipe insulation before repair", sizes="(max-width: 680px) 45vw, 22vw")}<figcaption><span class="badge badge--soft">Before</span></figcaption></figure>
        <figure>{pic("pipe-insulation-after", "New black pipe insulation fitted to the same heat pump after repair", sizes="(max-width: 680px) 45vw, 22vw")}<figcaption><span class="badge badge--gold">After</span></figcaption></figure>
      </div>
      <div class="card-body"><h3>Pipe insulation repair</h3><p>Sun and weather break down the lagging on your outdoor pipes, which wastes energy. We strip the damaged insulation and fit new, UV-resistant lagging.</p></div>
    </article>
    <article class="card reveal" id="healthy-homes"><div class="icon-chip">{icon("home")}</div><h3>Healthy Homes heating compliance</h3>
      <p>For landlords and property managers. We check your heat pump meets the Healthy Homes heating requirement for the main living room and give you a clear report for your records.</p>
      <ul class="check-list"><li>Heating capacity assessment for the main living room</li><li>Check existing heat pumps are working well with clean airflow</li><li>Digital report for your tenancy records</li><li>Annual maintenance plans for property managers</li></ul>
      <a class="more" href="/contact/?service=other#quote" data-service="other">Ask about Healthy Homes →</a></article>
  </div>
</div></section>"""
    process = f"""
<section class="section" aria-labelledby="how-title"><div class="wrap split">
  <div class="split-media tall reveal">{pic("cleaning-bag-setup", "Heat pump with a waterproof cleaning bag fitted underneath and a step ladder ready")}</div>
  <div class="stack reveal"><span class="eyebrow">How we work</span><h2 id="how-title">Clean, careful and mess-free.</h2>
    <p class="lead">We fit a waterproof cleaning bag under the indoor unit, lay drop sheets, and wash the dirt straight into the bag. You get clean air without the mess.</p>
    <ul class="check-list"><li>Indoor unit opened and protected before we start</li><li>Coils and fan washed with a non-corrosive cleaner</li><li>Outdoor unit cleared of leaves and pressure washed</li><li>Everything tested before we leave</li></ul>
    <div class="split-media" style="margin-top:12px">{pic("outdoor-unit-wash", "Outdoor heat pump unit being gently pressure washed")}</div>
  </div>
</div></section>"""
    give = f"""
<section class="section section--sage" id="giveaway" aria-labelledby="give-title"><div class="wrap giveaway">
  <a href="{e(FB_POST)}" target="_blank" rel="noopener" aria-label="Open our giveaway post on Facebook (opens in a new tab)">{pic("giveaway-promo", "Midha giveaway poster: win one free heat pump cleaning in Wellington", sizes="320px")}</a>
  <div class="stack"><span class="badge badge--urgent" style="align-self:flex-start">Next draw: <span data-next-draw>{NEXT_DRAW}</span></span>
    <h2 id="give-title">Win a free heat pump clean.</h2>
    <p class="lead">Every 3 months we give a free heat pump clean (our $79 Pro Clean) to one Wellington winner, drawn at random. Draws happen at the end of March, June, September and December.</p>
    <p>To enter, go to our giveaway post on Facebook and:</p>
    <ul class="check-list"><li>Like the post</li><li>Tag 3 friends in Wellington in the comments</li><li>Live in the Wellington region</li></ul>
    <div class="btn-row"><a class="btn btn--primary" href="{e(FB_POST)}" target="_blank" rel="noopener">Enter on Facebook <span class="visually-hidden">(opens in a new tab)</span></a></div>
    <p class="note">Free to enter. 18+ Wellington region residents only. <a href="/giveaway-terms/">Full terms and conditions</a>. This giveaway is run by Midha Limited and isn’t sponsored or run by Facebook.</p>
  </div>
</div></section>"""
    fq, fld = faq([
        ("Are your prices per heat pump?", "Yes. All package prices are per heat pump and include GST. For two heat pumps on the Elite Clean, the total is $258."),
        ("Which package should I choose?", "If your heat pump has been cleaned in the last year, Pro Clean is usually enough. Elite Clean is our most popular choice for a yearly service. Choose Comprehensive if you can smell mould or see black spots on the fan."),
        ("Why does my heat pump smell musty?", "Mould and bacteria grow on the damp coils and fan inside the indoor unit. A filter wipe won’t reach them. Our Elite and Comprehensive cleans wash them out, and Comprehensive adds an anti-mould treatment with a 3-month guarantee."),
        ("Why is my heat pump blowing cold air or using more power?", "Blocked filters, dirty coils and leaves in the outdoor unit make your heat pump work harder. A clean usually restores airflow and efficiency. If it still isn’t right, we’ll check for faults."),
        ("What does the 3-month mould-free guarantee cover?", "If mould comes back within 3 months of a Comprehensive Clean, we’ll come back and re-clean the unit for free."),
        ("How long does a clean take?", "Allow 1 to 2 hours per heat pump depending on the package and access. We’ll give you a time window when you book."),
    ], title="Heat pump questions")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Heat pump cleaning", "provider": {"@id": SITE + "/#business"},
              "areaServed": {"@type": "AdministrativeArea", "name": "Wellington Region"}, "offers": [
                  {"@type": "Offer", "name": n, "price": p, "priceCurrency": "NZD"} for n, p in (("Pro Clean", "79"), ("Elite Clean", "129"), ("Comprehensive Clean", "189"))]}
    body = f"""<main id="main">{hero}{packages_section()}{extras}{process}{give}{fq}{quote_section("Book your heat pump clean", "Choose a package below, or tell us what’s wrong and we’ll recommend one.")}</main>"""
    write("/heat-pump-cleaning/", head("Heat Pump Cleaning Wellington & Lower Hutt from $79 | Midha",
        "Heat pump deep cleaning in Wainuiomata, Lower Hutt, Upper Hutt, Tawa and Porirua. Pro $79, Elite $129, Comprehensive $189 per unit, GST incl.",
        "/heat-pump-cleaning/", [bld, fld, svc_ld]) + nav("/heat-pump-cleaning/") + body + footer())

def location_links(exclude=None):
    """Link list of every test & tag city page, plus the rural page."""
    items = "".join(f'<li><a href="/test-and-tag/{c["slug"]}/">{e(c["name"])}<span>{e(c["region"])}</span></a></li>'
                    for c in CITIES if c["slug"] != exclude)
    if exclude != RURAL[0]:
        items += f'<li><a href="/test-and-tag/{RURAL[0]}/">{e(RURAL[1])}<span>Farms, orchards, remote sites</span></a></li>'
    return f'<ul class="loc-grid">{items}</ul>'

TT_FAQ_SHARED = [
    ("How often does equipment need testing?", "It depends on the environment. Construction and hire equipment is usually tested every 3 months, factories and workshops every 6 months, and offices and other low-risk places every 12 months or longer. We’ll recommend the right interval for your site."),
    ("How much does test &amp; tag cost?".replace("&amp;", "&"), "It depends on how many items you have and where they are. Tell us roughly how many items and where your site is, and we’ll send a fixed-price quote that includes any travel, usually within 2 hours."),
    ("Do you provide certificates for audits?", "Yes. You’ll receive a full digital PDF register of every item tested, usually within 24 hours of the job."),
]

def tt_steps():
    steps = [("Tell us what you’ve got", "Roughly how many items, where your site is, and any times that suit."),
             ("Get a fixed quote", "One price that includes travel, so there are no surprises."),
             ("We test on site", f"Our team or one of our partner technicians tests to {STANDARD}, around your hours."),
             ("Get your register", "QR tags on every item, and your digital register usually within 24 hours.")]
    lis = "".join(f'<li class="card reveal"><span class="step-num">{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(steps))
    return f"""<section class="section" aria-labelledby="tt-how"><div class="wrap">
  <div class="section-head"><span class="eyebrow">How it works</span><h2 id="tt-how">Simple, wherever you are.</h2>
  <p>We’re based in Wellington and test right across New Zealand. Depending on where you are, we travel to you or send one of our partner technicians. Either way you get the same testing, tags and register.</p></div>
  <ol class="grid grid-4 steps">{lis}</ol>
</div></section>"""

def also_checks(head=True):
    """Cards linking to the medical and fire pages, shown on test & tag pages."""
    hd = ('<div class="section-head" style="margin-top:40px"><span class="eyebrow">Also available, NZ-wide</span>'
          '<h3 style="font-size:var(--fs-h3)">More safety checks in the same visit.</h3></div>') if head else ""
    return f"""{hd}<div class="grid grid-2">
    <a class="card card--lift reveal" href="{MED_PATH}"><div class="icon-chip" style="background:var(--c-bg)">{icon("cross")}</div><h3>Medical equipment testing</h3><p>Electrical safety testing of beds, hoists, pumps and other medical equipment to {MED_STD}, for clinics, aged care and equipment providers.</p><span class="more">Medical testing details →</span></a>
    <a class="card card--lift reveal" href="{FIRE_PATH}"><div class="icon-chip" style="background:var(--c-bg)">{icon("flame")}</div><h3>Fire extinguisher &amp; blanket checks</h3><p>Yearly fire extinguisher testing to {FIRE_STD}, fire blanket checks, tags and a register you can show anyone who asks.</p><span class="more">Fire check details →</span></a>
  </div>"""

def steps_block(sid, title, intro, steps, eyebrow="How it works"):
    lis = "".join(f'<li class="card reveal"><span class="step-num">{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(steps))
    return f"""<section class="section" aria-labelledby="{sid}"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{eyebrow}</span><h2 id="{sid}">{title}</h2>
  <p>{intro}</p></div>
  <ol class="grid grid-4 steps">{lis}</ol>
</div></section>"""

MED_SVG = """<svg viewBox="0 0 220 300" role="img" aria-label="Illustration of a medical equipment test label reading Tested, AS/NZS 3551">
<rect x="20" y="20" width="180" height="260" rx="24" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="4"/>
<rect x="82" y="40" width="56" height="56" rx="14" fill="#E2E8E4" stroke="#1C1C1C" stroke-width="4"/>
<path d="M110 54v28M96 68h28" stroke="#1C1C1C" stroke-width="6" stroke-linecap="round"/>
<text x="110" y="136" text-anchor="middle" font-family="General Sans, sans-serif" font-weight="700" font-size="26" fill="#1C1C1C">TESTED</text>
<text x="110" y="164" text-anchor="middle" font-family="Switzer, sans-serif" font-weight="600" font-size="16" fill="#6E6354">AS/NZS 3551</text>
<line x1="44" y1="186" x2="176" y2="186" stroke="#978B7A" stroke-width="3" stroke-dasharray="8 6"/>
<text x="44" y="214" font-family="Switzer, sans-serif" font-weight="600" font-size="14" fill="#1C1C1C">Electrical safety ✓</text>
<text x="44" y="238" font-family="Switzer, sans-serif" font-weight="600" font-size="14" fill="#1C1C1C">Visual inspection ✓</text>
<text x="44" y="262" font-family="Switzer, sans-serif" font-size="13" fill="#4A4A45">Next test due</text>
</svg>"""

FIRE_SVG = """<svg viewBox="0 0 220 300" role="img" aria-label="Illustration of a fire extinguisher with a maintenance tag">
<path d="M92 44h36v18H92Z" fill="#1C1C1C"/>
<path d="M128 50h34l10 14" fill="none" stroke="#1C1C1C" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M84 64h52v14H84Z" fill="#1C1C1C"/>
<rect x="66" y="76" width="88" height="196" rx="36" fill="#B9382C" stroke="#1C1C1C" stroke-width="4"/>
<circle cx="110" cy="112" r="14" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="3"/>
<path d="M110 112l6-7" stroke="#1C1C1C" stroke-width="3" stroke-linecap="round"/>
<rect x="74" y="150" width="72" height="70" rx="8" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="3"/>
<text x="110" y="178" text-anchor="middle" font-family="General Sans, sans-serif" font-weight="700" font-size="12" fill="#1C1C1C">NZS 4503</text>
<text x="110" y="200" text-anchor="middle" font-family="Switzer, sans-serif" font-weight="600" font-size="11" fill="#6E6354">CHECKED</text>
<path d="M136 64c22 6 34 22 30 52" fill="none" stroke="#978B7A" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 10"/>
</svg>"""

def medical_page():
    path = MED_PATH
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", "/test-and-tag/"), ("Medical equipment testing", None)],
        "Medical test &amp; tag · NZ-wide", f"Medical equipment testing to {MED_STD}.",
        "Electrical safety testing and labelling of medical equipment for clinics, aged care and equipment providers across New Zealand, with an audit-ready report.",
        badge=f'<span class="badge badge--gold">{MED_STD}</span>')
    equip = ["Electric hospital &amp; care beds", "Patient hoists &amp; ceiling hoists", "Electric lift &amp; recliner chairs", "Air mattress pumps",
             "Suction pumps", "Oxygen concentrators", "Nebulisers", "CPAP machines", "Examination lights", "Electric treatment couches &amp; tables",
             "Sterilisers &amp; autoclaves", "Power wheelchair &amp; scooter chargers"]
    who = ["GP clinics &amp; medical centres", "Dental clinics", "Physiotherapy", "Chiropractic &amp; osteopathy", "Podiatry",
           "Aged care &amp; rest homes", "Hospices", "Disability support providers", "Home-care equipment providers", "Medical equipment hire"]
    sec = f"""
<section class="section" aria-labelledby="med-what"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Why medical equipment is different</span><h2 id="med-what">Normal test &amp; tag doesn’t cover medical devices.</h2>
    <p class="lead">A normal {STANDARD} tag doesn’t count for medical equipment. Under the Electricity (Safety) Regulations 2010, the owner of an electrical medical device must have it checked regularly to {MED_STD}, which has tighter safety limits.</p>
    <p>We test your medical equipment to {MED_STD} using a tester made for the job, and test everything else in the building to {STANDARD} in the same visit.</p>
    <ul class="check-list">
      <li>Visual inspection of each device, its cord and plug</li>
      <li>Protective earth, insulation and leakage current tests to {MED_STD}</li>
      <li>A label on each device showing the test date, next due date, tests done and the standard</li>
      <li>An asset register and report you can show at your accreditation audit</li>
      <li>Faulty items clearly tagged out of service and listed in your report</li>
      <li>Normal test &amp; tag of your other appliances in the same visit</li>
    </ul>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="#quote" data-service="medical">Get a medical testing quote</a></div>
  </div>
  <div class="tag-illus reveal">{MED_SVG}</div>
</div></section>
<section class="section section--sage" aria-labelledby="med-equip"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we test</span><h2 id="med-equip">Equipment we test.</h2>
  <p>We test everyday medical equipment, such as beds, hoists, chairs and pumps. Tell us what you have and we’ll confirm what we can test.</p></div>
  <ul class="chips">{''.join(f'<li>{x}</li>' for x in equip)}</ul>
  <div class="grid grid-2" style="margin-top:32px">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Specialist equipment</h3><p>We don’t test patient monitors, ECG machines, infusion pumps or defibrillators. These need a biomedical engineer, and we’re happy to suggest one.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("bolt")}</div><h3>Body protected areas</h3><p>Treatment rooms with medical-grade 10 mA safety switches need a yearly check and certificate from a registered electrician. We can arrange this for you with a registered electrician.</p></div>
  </div>
</div></section>
<section class="section" aria-labelledby="med-who"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Who we test for</span><h2 id="med-who">Clinics, care providers and equipment suppliers.</h2></div>
  <ul class="chips">{''.join(f'<li>{x}</li>' for x in who)}</ul>
</div></section>
{steps_block("med-how", "Simple, and around your patients.", "We test right across New Zealand. Depending on where you are, we travel to you or send one of our partner technicians.", [
        ("Send us your list", "Roughly what medical equipment you have, plus how many other appliances, and where."),
        ("Get a fixed quote", "One price that includes travel, so there are no surprises."),
        ("We test on site", "Room by room, around your clinic hours, so patients aren’t disrupted."),
        ("Get your report", "Labels on every device, and an audit-ready register with next due dates.")])}"""
    fq, fld = faq([
        ("Is medical equipment testing a legal requirement?", f"Yes. Under regulation 91 of the Electricity (Safety) Regulations 2010, the owner of an electrical medical device must make sure it is checked regularly to {MED_STD}. Using a device that hasn’t been checked is an offence, except in an emergency. The person who tests it gives you a record of the results."),
        ("How often does medical equipment need testing?", "At least every 12 months, or more often if the manufacturer says so. New equipment should also be tested before it’s first used, and after any repair."),
        ("Isn’t normal test & tag enough?", f"No. A normal {STANDARD} tag doesn’t count for medical devices, because medical equipment has tighter safety limits. Your other appliances, like kettles, computers and staff fridges, still get normal test &amp; tag, and we do both in one visit."),
        ("Can you test without disrupting patients?", "Yes. We work room by room around your clinic hours, or before opening and after closing."),
        ("Do you test patient monitors, ECGs or infusion pumps?", "No. These need specialist biomedical testing. We’re happy to suggest a biomedical engineer, and we can test the rest of your equipment."),
        ("Will the report help with our audit?", "Yes. You get a register listing every device with its result, test date and next due date, which you can show your auditor."),
    ], title="Medical equipment testing questions", sage=True)
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": "Medical equipment testing",
              "serviceType": f"Medical electrical equipment testing ({MED_STD})", "provider": {"@id": SITE + "/#business"},
              "areaServed": {"@type": "Country", "name": "New Zealand"}, "url": SITE + path}
    body = f"""<main id="main">{hero}{sec}{fq}{quote_section("Get a medical equipment testing quote", "Tell us roughly what equipment you have and where, and we’ll send a fixed price.", default="medical")}</main>"""
    write(path, head(f"Medical Equipment Testing NZ | {MED_STD} Test & Tag | Midha",
        f"Medical equipment test and tag to {MED_STD} across NZ: beds, hoists, pumps and more for GP clinics, dental, physio and aged care. Audit-ready reports.",
        path, [bld, fld, svc_ld]) + nav(path) + body + footer())

def fire_page():
    path = FIRE_PATH
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", "/test-and-tag/"), ("Fire extinguisher checks", None)],
        "Fire safety checks · NZ-wide", "Fire extinguisher and fire blanket checks.",
        f"Yearly fire extinguisher testing to {FIRE_STD} and fire blanket checks for workplaces across New Zealand, often in the same visit as your test &amp; tag.",
        badge=f'<span class="badge badge--gold">NZS 4503</span>')
    who = ["Offices", "Cafés &amp; commercial kitchens", "Workshops &amp; factories", "Construction sites", "Schools &amp; early learning", "Retail stores",
           "Warehouses", "Rental &amp; commercial buildings", "Community halls &amp; marae", "Farms", "Clinics &amp; aged care"]
    sec = f"""
<section class="section" aria-labelledby="fire-what"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">What’s included</span><h2 id="fire-what">Checked, tagged and on the register.</h2>
    <p class="lead">Most building owners (not private homes) must keep their fire extinguishers and fire blankets maintained to {FIRE_STD}. We check and test yours, tag each one, and keep a register so you know what’s due.</p>
    <ul class="check-list">
      <li>Inspection and testing of portable fire extinguishers to {FIRE_STD}</li>
      <li>Pressure gauge, pin and seal, hose, nozzle, label and bracket checked</li>
      <li>Fire blankets checked: in place, easy to reach, undamaged, with pull tabs intact</li>
      <li>A maintenance tag on every extinguisher</li>
      <li>A fire equipment register and report for your records</li>
      <li>Anything that fails is clearly marked, with advice on what to do next</li>
    </ul>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="#quote" data-service="fire">Get a fire check quote</a></div>
  </div>
  <div class="tag-illus reveal">{FIRE_SVG}</div>
</div></section>
<section class="section section--sage" aria-labelledby="fire-often"><div class="wrap">
  <div class="section-head"><span class="eyebrow">How often</span><h2 id="fire-often">What NZS 4503 asks for.</h2></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("clock")}</div><h3>Every 12 months</h3><p>Most workplaces need their extinguishers and fire blankets checked once a year.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Every 6 months in harsh places</h3><p>Extinguishers in corrosive, dusty, outdoor or high-vibration areas are checked twice a year.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("wrench")}</div><h3>Pressure test every 5 years</h3><p>We don’t refill or pressure test extinguishers ourselves. When one is due, or has been used, we arrange it through our specialist partner.</p></div>
  </div>
</div></section>
<section class="section" aria-labelledby="fire-self"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Between our visits</span><h2 id="fire-self">A quick monthly check for your team.</h2>
    <p class="lead">It takes a minute. If anything looks wrong, call us.</p>
    <ul class="check-list">
      <li>Each extinguisher is in its place and nothing is blocking it</li>
      <li>The pin and seal are in place</li>
      <li>The gauge needle is in the green</li>
      <li>No dents, rust, leaks or damaged hoses</li>
      <li>The fire blanket is in place, with both pull tabs showing</li>
    </ul>
  </div>
  <div class="stack reveal"><div class="card"><h3>Who we check for</h3><ul class="chips">{''.join(f'<li>{x}</li>' for x in who)}</ul></div></div>
</div></section>"""
    fq, fld = faq([
        ("How often do fire extinguishers need servicing in NZ?", f"Under {FIRE_STD}, most workplaces need their extinguishers serviced every 12 months. Extinguishers in harsh places, such as corrosive, dusty or outdoor areas, are checked every 6 months. Each extinguisher also needs a pressure test every 5 years."),
        ("Do I have to have fire extinguishers?", f"It depends on your building and what you store. Fire and Emergency NZ rules require them in some buildings, and workplaces that store flammable substances like fuel or solvents may need them too. If you do have extinguishers or fire blankets, they must be maintained to {FIRE_STD}."),
        ("Do fire blankets need checking?", f"Yes. Fire blankets are covered by {FIRE_STD} along with extinguishers. We check they’re in place, easy to reach and undamaged. A blanket that has been used should be replaced."),
        ("Can you refill or pressure test extinguishers?", "We don’t do refills or pressure tests ourselves. We arrange them through our specialist partner and give you the price before anything is sent away."),
        ("Can you do this with our test & tag?", "Yes. Most customers book both together, so one visit covers your electrical equipment and your fire extinguishers."),
    ], title="Fire extinguisher questions", sage=True)
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": "Fire extinguisher and fire blanket checks",
              "serviceType": f"Fire extinguisher inspection and testing ({FIRE_STD})", "provider": {"@id": SITE + "/#business"},
              "areaServed": {"@type": "Country", "name": "New Zealand"}, "url": SITE + path}
    body = f"""<main id="main">{hero}{sec}{fq}{quote_section("Get a fire extinguisher check quote", "Tell us roughly how many extinguishers and fire blankets you have and where.", default="fire")}</main>"""
    write(path, head(f"Fire Extinguisher Testing NZ | NZS 4503 & Fire Blankets | Midha",
        f"Fire extinguisher testing to {FIRE_STD} and fire blanket checks for NZ workplaces. Tags, a fire equipment register, and test & tag in the same visit.",
        path, [bld, fld, svc_ld]) + nav(path) + body + footer())

def test_tag():
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", None)], "Workplace electrical safety · NZ-wide",
        "Test &amp; tag across New Zealand.",
        f"Electrical testing and tagging to {STANDARD} for workplaces from Whangārei to Invercargill, with QR-coded tags, RCD testing and a digital register you can show any auditor.",
        badge=f'<span class="badge badge--gold">{STANDARD}</span>')
    body_sec = f"""
<section class="section" aria-labelledby="tt-what"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">What’s included</span><h2 id="tt-what">Everything you need for compliance.</h2>
    <p class="lead">Under the Health and Safety at Work Act, businesses must keep electrical equipment safe. Regular testing and tagging to {STANDARD} is the most common way to show you’re doing that.</p>
    <ul class="check-list">
      <li>Inspection and testing to {STANDARD}</li>
      <li>Single-phase and three-phase equipment, power tools, leads and appliances</li>
      <li>RCD (safety switch) trip-time and push-button testing with logs</li>
      <li>A QR-coded tag on every item for instant digital lookup</li>
      <li>Digital PDF register, usually within 24 hours</li>
      <li>Reminders before your retests are due</li>
    </ul>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="/contact/?service=test-tag#quote" data-service="test-tag">Get a test &amp; tag quote</a></div>
  </div>
  <div class="tag-illus reveal">{TAG_SVG}</div>
</div></section>
<section class="section section--sage" id="locations" aria-labelledby="tt-where"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Where we test</span><h2 id="tt-where">Test &amp; tag in every main centre.</h2>
  <p>Choose your city to see what we do there. Not near a main centre? Our regional and rural service covers farms, orchards and remote sites anywhere in the country.</p></div>
  {location_links()}
</div></section>
{tt_steps()}
<section class="section section--sage" aria-labelledby="tt-who"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Who we test for</span><h2 id="tt-who">From cafés to construction sites.</h2></div>
  <ul class="chips"><li>Workshops &amp; factories</li><li>Construction sites</li><li>Offices</li><li>Cafés &amp; restaurants</li><li>Schools &amp; early learning</li><li>Retail stores</li><li>Warehouses</li><li>Farms &amp; orchards</li><li>Hotels &amp; motels</li><li>Multi-site businesses</li><li>Rental properties</li><li>Community halls</li><li>Medical &amp; dental clinics</li><li>Aged care</li></ul>
  <div class="grid grid-3" style="margin-top:32px">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("qr")}</div><h3>Smart QR tags</h3><p>Scan any tag to see its test history. No more hunting through paper logbooks.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("clock")}</div><h3>Around your hours</h3><p>Early starts before the tools come out, or quiet times so your customers aren’t disturbed.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Faulty gear flagged</h3><p>Anything that fails is clearly tagged out of service and listed in your register, so you know what to repair or replace.</p></div>
  </div>
</div></section>"""
    more = f"""<section class="section" aria-labelledby="tt-more"><div class="wrap">
  <div class="section-head"><span class="eyebrow">More safety checks · NZ-wide</span><h2 id="tt-more">Medical equipment and fire extinguishers too.</h2>
  <p>Book them with your test &amp; tag and one visit covers the lot.</p></div>
  {also_checks(head=False)}
</div></section>"""
    revs = "".join(review_card(r) for r in REVIEWS if r[2] == "Test & Tag")
    rev = f"""<section class="section" aria-labelledby="tt-rev"><div class="wrap"><div class="section-head"><span class="eyebrow">What clients say</span><h2 id="tt-rev">Trusted by local businesses.</h2></div><div class="grid grid-3">{revs}</div></div></section>"""
    fq, fld = faq(TT_FAQ_SHARED + [
        ("Do you cover my area?", 'Yes. We test and tag across New Zealand. See the <a href="#locations">list of locations</a>, or if you’re rural or remote, our <a href="/test-and-tag/regional-rural-nz/">regional and rural page</a>.'),
        ("Who does the testing outside Wellington?", f"Depending on where you are, we travel to you or send one of our partner technicians. Everyone tests to {STANDARD} and uses the same QR tags and digital register."),
        ("Can you test sites in different cities?", "Yes. Tell us where your sites are and roughly how many items each one has. We’ll quote for them together and keep a separate register for each site."),
        ("How does the QR tagging work?", "Each item gets a tag with a unique QR code. Scan it with a phone to see when it was tested, the result and when the next test is due."),
        ("Do you test RCDs (safety switches)?", "Yes. We test portable and fixed RCDs for trip time and push-button operation, and record the results in your register."),
    ], title="Test & tag questions")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": "Test and tag", "serviceType": f"Electrical test and tag ({STANDARD})",
              "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "Country", "name": "New Zealand"}}
    body = f"""<main id="main">{hero}{body_sec}{more}{rev}{fq}{quote_section("Get a test & tag quote", "Let us know roughly how many items and where they are, and we’ll come back with a fixed price.", default="test-tag")}</main>"""
    write("/test-and-tag/", head(f"Test and Tag NZ | {STANDARD} | Midha Limited",
        f"{STANDARD} test and tag for workplaces across NZ: Auckland, Hamilton, Tauranga, Wellington, Christchurch, Dunedin and more. QR tags, digital register.",
        "/test-and-tag/", [bld, fld, svc_ld]) + nav("/test-and-tag/") + body + footer())

def city_page(c):
    name = c["name"]
    path = f"/test-and-tag/{c['slug']}/"
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", "/test-and-tag/"), (name, None)],
        f"Test &amp; tag · {e(c['region'])}", f"Test and tag {e(name)}.", e(c["lead"]),
        badge=f'<span class="badge badge--gold">{STANDARD}</span>')
    intro = "".join(('<p class="lead">' if i == 0 else "<p>") + e(p) + "</p>" for i, p in enumerate(c["intro"]))
    inds = "".join(f"<li>{e(x)}</li>" for x in c["industries"])
    near = "".join(f"<li>{e(x)}</li>" for x in c["nearby"])
    sec = f"""
<section class="section" aria-labelledby="city-intro"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Test &amp; tag in {e(name)}</span><h2 id="city-intro">Safe, tagged and audit-ready.</h2>
    {intro}
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="#quote" data-service="test-tag">Get your {e(name)} quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
  <div class="stack reveal">
    <div class="card"><h3>Who we test for in {e(name)}</h3><ul class="chips">{inds}</ul></div>
    <div class="card"><h3>Areas we cover</h3><ul class="chips">{near}</ul></div>
  </div>
</div></section>
<section class="section section--sage" aria-labelledby="city-inc"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Every job includes</span><h2 id="city-inc">The same thorough service, wherever you are.</h2></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("tag")}</div><h3>Tested to {STANDARD}</h3><p>Tools, appliances, leads and RCDs inspected and tested, with results recorded.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("qr")}</div><h3>QR tags &amp; digital register</h3><p>Every item gets a QR tag, and your PDF register usually arrives within 24 hours.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("dollar")}</div><h3>Fixed quote, travel included</h3><p>You know the full price before we book, with reminders before your retests are due.</p></div>
  </div>
  {also_checks()}
</div></section>
{tt_steps()}"""
    fq, fld = faq(c["faqs"] + TT_FAQ_SHARED[:2], title=f"Test & tag in {name}: questions")
    others = f"""<section class="section section--sage" aria-labelledby="city-more"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Other locations</span><h2 id="city-more">We also test and tag in…</h2></div>
  {location_links(exclude=c['slug'])}
</div></section>"""
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": f"Test and tag {name}",
              "serviceType": f"Electrical test and tag ({STANDARD})", "provider": {"@id": SITE + "/#business"},
              "areaServed": {"@type": "City", "name": name.replace(" & ", " and "), "containedInPlace": {"@type": "AdministrativeArea", "name": c["region"]}},
              "url": SITE + path}
    body = f"""<main id="main">{hero}{sec}{fq}{others}{quote_section(f"Get a test & tag quote for {name}", "Tell us roughly how many items and where your site is, and we’ll send a fixed price that includes travel.", default="test-tag")}</main>"""
    desc = f"Test and tag in {name} to {STANDARD}. {c['industries'][0]}, {c['industries'][1].lower()} and more. QR tags, RCD testing, digital register, fixed quotes."
    write(path, head(f"Test and Tag {name} | {STANDARD} | Midha Limited", desc, path, [bld, fld, svc_ld])
          + nav(path) + body + footer())

def rural_page():
    path = f"/test-and-tag/{RURAL[0]}/"
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", "/test-and-tag/"), (RURAL[1], None)],
        "Test &amp; tag · anywhere in NZ", "Test and tag for regional and rural New Zealand.",
        f"Farms, orchards, vineyards, rural schools, marae and remote work sites, tested to {STANDARD} with QR tags and a digital register.",
        badge=f'<span class="badge badge--gold">{STANDARD}</span>')
    who = "".join(f"<li>{e(x)}</li>" for x in ["Farms & dairy sheds", "Orchards & packhouses", "Vineyards & wineries", "Shearing sheds & woolsheds", "Rural schools", "Marae", "Community & sports halls", "Holiday parks", "Remote work sites", "Rural contractors"])
    regions = "".join(f"<li>{e(x)}</li>" for x in NZ_REGIONS)
    sec = f"""
<section class="section" aria-labelledby="rural-intro"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Not near a main centre?</span><h2 id="rural-intro">We still come to you.</h2>
    <p class="lead">Rural and remote sites get the same testing, QR tags and digital register as a city office. We plan visits to each region in advance, and your fixed quote includes travel.</p>
    <p>Farm gear and rural workplaces are tough on equipment. Leads get dragged through sheds and paddocks, tools get wet, and plugs take a beating. Regular testing finds damaged cords and faulty gear before they hurt someone.</p>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="#quote" data-service="test-tag">Get a rural quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
  <div class="stack reveal">
    <div class="card"><h3>Who we test for</h3><ul class="chips">{who}</ul></div>
    <div class="card"><h3>Regions we cover</h3><ul class="chips">{regions}</ul></div>
  </div>
</div></section>
{tt_steps()}
<section class="section" style="padding-top:0"><div class="wrap">{also_checks()}</div></section>"""
    fq, fld = faq([
        ("How much does travel to a rural site cost?", "Travel is included in your fixed quote, so you’ll know the full price before you book."),
        ("What do you need to know to quote?", "Where your site is, roughly how many items need testing, and any timing that suits you, such as before harvest, calving or a new season starts."),
        ("Can neighbouring farms or businesses book together?", "Yes. If you know others nearby who need testing, let us know and we’ll quote for the visits together."),
    ] + TT_FAQ_SHARED[:1], title="Rural test & tag questions")
    others = f"""<section class="section section--sage" aria-labelledby="rural-more"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Main centres</span><h2 id="rural-more">Near a city? See your local page.</h2></div>
  {location_links(exclude=RURAL[0])}
</div></section>"""
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": "Rural test and tag New Zealand",
              "serviceType": f"Electrical test and tag ({STANDARD})", "provider": {"@id": SITE + "/#business"},
              "areaServed": {"@type": "Country", "name": "New Zealand"}, "url": SITE + path}
    body = f"""<main id="main">{hero}{sec}{fq}{others}{quote_section("Get a rural test & tag quote", "Tell us where you are and roughly how many items need testing.", default="test-tag")}</main>"""
    write(path, head(f"Rural Test and Tag NZ | Farms, Orchards & Remote Sites | Midha",
        f"{STANDARD} test and tag for farms, orchards, vineyards, rural schools, marae and remote sites anywhere in New Zealand. Fixed quotes with travel included.",
        path, [bld, fld, svc_ld]) + nav(path) + body + footer())

def electrical():
    hero, bld = page_hero([("Home", "/"), ("Electrical Services", None)], "Electrical services",
        "Lighting, power points and repairs, done tidily.",
        "Light installations, LED downlights, security and sensor lights, new power points, and cord and lead repairs for homes and businesses across Greater Wellington.",
        badge=f'<span class="badge badge--gold">{EST}</span>')
    hero = hero.replace('<span class="eyebrow">Electrical services</span>', '<span class="eyebrow">Electrical services · Greater Wellington</span>')
    items = [
        ("bulb", "Light installations", "Replacements for tired or broken lights, plus new light fittings and pendants, inside and out."),
        ("bolt", "LED downlights", "Swap old halogens for energy-efficient LED downlights that run cooler and cost less to run."),
        ("shield", "Security & sensor lights", "Motion-sensor and security lighting for driveways, entrances and yards."),
        ("plug", "Power points", "Broken power points replaced, plus extra or relocated power points, including double and USB outlets."),
        ("wrench", "Cord & lead repairs", "Damaged extension leads and appliance cords repaired or replaced, often on the spot."),
    ]
    cards = "".join(f'<article class="card card--lift reveal"><div class="icon-chip">{icon(i)}</div><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, t, d in items)
    cards += f'<article class="card card--ink on-dark reveal"><h3>Not sure what you need?</h3><p>Describe the job and we’ll let you know how we can help.</p><a class="btn btn--gold" style="margin-top:auto;align-self:flex-start" href="/contact/?service=electrical#quote" data-service="electrical">Ask us</a></article>'
    sec = f"""
<section class="section section--sage" aria-labelledby="el-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we do</span><h2 id="el-title">Electrical jobs we take on.</h2></div>
  <div class="grid grid-3">{cards}</div>
</div></section>
<section class="section" aria-labelledby="el-who"><div class="wrap">
  <div class="card reveal" style="max-width:860px">
    <div class="icon-chip" style="background:var(--c-sage)">{icon("shield")}</div>
    <h2 id="el-who" style="font-size:var(--fs-h3)">Who does the work.</h2>
    <p>Midha is a {EST}. We do repairs and like-for-like replacements ourselves. <strong>New installations</strong>, such as extra power points or new lights, are done by a <strong>registered electrician</strong>, with us assisting. Either way, you get one fixed quote.</p>
  </div>
</div></section>
<section class="section" aria-labelledby="el-why" style="padding-top:0"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">How we work</span><h2 id="el-why">Clear quotes, clean work.</h2>
    <p class="lead">We quote a fixed price before we start, turn up when we say we will, and leave your place as tidy as we found it.</p>
    <ul class="check-list"><li>Fixed, upfront quotes</li><li>New installations done by a registered electrician</li><li>Drop sheets and clean boots</li><li>Old fittings taken away</li><li>Everything tested before we leave</li></ul>
  </div>
  <div class="tag-illus reveal">{BULB_SVG}</div>
</div></section>"""
    fq, fld = faq([
        ("Do you do small jobs?", "Yes. Swapping a light fitting, replacing a broken power point or repairing a cord is exactly the kind of job we’re happy to take on."),
        ("Who does the electrical work?", f"Midha is a {EST}. We do repairs and like-for-like replacements ourselves. New installations, like extra power points or new lights, are done by a registered electrician, with us assisting. You still get one fixed quote."),
        ("Can you switch my old downlights to LED?", "Yes. LED downlights use far less power and run cooler than halogens. We’ll quote for the number of lights you want changed."),
        ("How do I get a price?", 'Fill in the quote form or call <a href="tel:' + TEL + '">' + PHONE + '</a> with a quick description and a photo if you can. We’ll come back with a fixed price.'),
    ], title="Electrical questions")
    body = f"""<main id="main">{hero}{sec}{fq}{quote_section("Get an electrical quote", "Tell us what you’d like done, and add a photo by email if it helps.", default="electrical")}</main>"""
    write("/electrical-services/", head("Electrical Services Wellington | Lighting & Power Points | Midha",
        "Light installations, LED downlights, security and sensor lights, power points and cord repairs across Lower Hutt, Upper Hutt and Wellington.",
        "/electrical-services/", [bld, fld, {"@context": "https://schema.org", "@type": "Service", "name": "Electrical services", "serviceType": "Lighting, power points and cord repairs",
            "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "AdministrativeArea", "name": "Wellington Region"}}]) + nav("/electrical-services/") + body + footer())

def areas_page():
    hero, bld = page_hero([("Home", "/"), ("Service Areas", None)], "Heat pump cleaning &amp; electrical · Greater Wellington", "Heat pump and electrical service areas.",
        'Heat pump cleaning and electrical work cover the Hutt Valley, Wellington’s northern suburbs and Porirua from our base in Wainuiomata. Need test &amp; tag? We cover <a href="/test-and-tag/#locations">all of New Zealand</a>.')
    cards = "".join(f"""<article class="card area-card reveal" id="{slug(n)}"><h2 style="font-size:var(--fs-h3)">{e(n)}</h2><span class="badge badge--soft">{e(sp)}</span><p>{e(d)}</p><ul>{''.join(f'<li>{e(s)}</li>' for s in subs)}</ul>
<a class="more" href="/contact/#quote">Book in {e(n.split(' &')[0])} →</a></article>""" for n, sp, d, subs in AREAS)
    sec = f"""<section class="section section--sage"><div class="wrap"><div class="grid grid-3">{cards}</div>
<p class="note" style="margin-top:24px">Typical booking times shown. Urgent callouts are available. Just call {PHONE}.</p></div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section()}</main>"""
    write("/service-areas/", head("Heat Pump & Electrical Areas | Hutt Valley & Porirua | Midha",
        "Heat pump cleaning and electrical work in Wainuiomata, Lower Hutt, Upper Hutt, Tawa, Newlands and Porirua. Test & tag is available across New Zealand.",
        "/service-areas/", [bld]) + nav("/service-areas/") + body + footer())

def reviews_page():
    hero, bld = page_hero([("Home", "/"), ("Reviews", None)], "5.0 Google rating", "What our customers say.",
        "Feedback from business owners, site managers and homeowners across Greater Wellington.")
    cards = "".join(review_card(r) for r in REVIEWS)
    sec = f"""<section class="section section--sage"><div class="wrap"><div class="grid grid-3">{cards}</div></div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section("Experience it for yourself")}</main>"""
    write("/reviews/", head("Customer Reviews | Midha Limited Wellington",
        "Read reviews from Wellington homeowners and businesses who use Midha Limited for test & tag, heat pump cleaning and electrical work.",
        "/reviews/", [bld]) + nav("/reviews/") + body + footer())

def about_page():
    hero, bld = page_hero([("Home", "/"), ("About", None)], "100% Kiwi owned &amp; operated", "About Midha Limited",
        "Keeping your whānau, team and property safe and comfortable, with straightforward local service.", ctas=False)
    sec = f"""
<section class="section"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Our story</span><h2>Safety, reliability and clean air.</h2>
    <p class="lead">Midha Limited started with a simple idea: every Kiwi workplace and home deserves reliable safety compliance and heating care, without red tape or hidden fees.</p>
    <p>Based in Wainuiomata, we look after heat pumps and electrical work across Lower Hutt, Upper Hutt, Tawa, Newlands and Porirua. Right across New Zealand, we test and tag workplaces, test medical equipment and check fire extinguishers. We combine careful technical work with friendly, approachable service.</p>
    <p class="note">Midha Limited is a registered New Zealand company, run by a {EST}.</p>
  </div>
  <div class="split-media reveal">{pic("indoor-coil-clean", "Midha technician cleaning an indoor heat pump coil")}</div>
</div></section>
<section class="section section--sage"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we stand for</span><h2>Our commitments.</h2></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Safety without shortcuts</h3><p>Electrical faults cost lives and livelihoods. We follow the standards fully, every time.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("dollar")}</div><h3>Honest fixed pricing</h3><p>What we quote is what you pay. No surprise travel, admin or disposal fees.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("home")}</div><h3>Respect for your place</h3><p>Clean boots, drop sheets and genuine care in every home and workplace.</p></div>
  </div>
</div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section()}</main>"""
    write("/about/", head("About Midha Limited | Wainuiomata, Wellington",
        "Midha Limited is a Kiwi-owned business in Wainuiomata: test & tag across New Zealand, plus heat pump cleaning and electrical work in Greater Wellington.",
        "/about/", [bld]) + nav("/about/") + body + footer())

def contact_page():
    hero, bld = page_hero([("Home", "/"), ("Contact", None)], "Reply within 2 hours", "Contact Midha Limited",
        f"Call or text {PHONE}, email {EMAIL}, or send the form below. We’re available {HOURS}, with urgent callouts available.", ctas=False)
    zone = f"""<section class="section section--sage"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Our base</span><h2>Where we work.</h2>
  <p class="lead">Heat pump cleaning and electrical work: Wainuiomata, Petone, Gracefield, Epuni, Waterloo, Silverstream, Trentham, Tawa, Newlands, Johnsonville and Porirua.</p>
  <p>Test &amp; tag, medical equipment testing and fire extinguisher checks: anywhere in New Zealand. <a href="/test-and-tag/#locations">See test &amp; tag locations</a>.</p></div>
  <ul class="chips"><li>No travel surcharge in Wainuiomata</li><li>Same day / next day in Wainui</li><li>After-hours slots for businesses</li><li>Urgent callouts available</li></ul>
</div></section>"""
    body = f"""<main id="main">{hero}{quote_section("Book a service or request a quote", "Test & tag, medical equipment, fire extinguishers, a heat pump clean or an electrical job? Tell us what you need.")}{zone}</main>"""
    write("/contact/", head("Contact Midha Limited | Book Test & Tag, Heat Pump or Electrical",
        f"Get a free, fixed-price quote. Call {PHONE} or email {EMAIL}. Test & tag across New Zealand; heat pumps and electrical in Greater Wellington.",
        "/contact/", [bld]) + nav("/contact/") + body + footer())

def simple(path, title, desc, h1, inner, robots=None):
    hd = head(title, desc, path)
    if robots: hd = hd.replace("<link rel=\"canonical\"", f'<meta name="robots" content="{robots}">\n<link rel="canonical"')
    if path == "/thanks/": hd = hd.replace("<body>", "<body data-thanks>")
    write(path, hd + nav(path) + f'<main id="main"><section class="page-hero"><div class="wrap"><h1>{h1}</h1></div></section><section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{inner}</div></div></section></main>' + footer())

def misc():
    simple("/thanks/", "Thanks | Midha Limited", "Thanks for your enquiry.", "Thanks, we’ve got your request.",
           f'<p class="lead">We’ll be in touch within 2 hours during business hours ({HOURS}). If it’s urgent, call <a href="tel:{TEL}">{PHONE}</a>.</p><p><a class="btn btn--primary" href="/">Back to home</a></p>', robots="noindex")
    updated = "16 October 2026"
    giveaway_updated = "21 October 2026"
    contact = f'<a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE}'
    simple("/privacy/", "Privacy Policy | Midha Limited", "How Midha Limited collects, uses, shares and protects your personal information under the New Zealand Privacy Act 2020.", "Privacy policy",
           f"""<p class="note">Last updated {updated}</p>
<p class="lead">Midha Limited (“we”, “us”) respects your privacy. This policy explains what personal information we collect, why, who we share it with, and your rights under the New Zealand Privacy Act 2020.</p>
<h2>Who we are</h2>
<p>Midha Limited is a New Zealand company based in Wainuiomata, Lower Hutt. We provide test &amp; tag, medical equipment testing and fire extinguisher checks across New Zealand, and heat pump cleaning and electrical services in the Wellington region. For anything about your personal information, contact our privacy officer at {contact}.</p>
<h2>What we collect</h2>
<ul>
  <li><strong>When you ask for a quote or book a job:</strong> your name, phone number, email, suburb or town, the service you need and any job details you give us.</li>
  <li><strong>When we do the job:</strong> the site address, an on-site contact person, access details, and job records such as test &amp; tag, medical equipment and fire equipment registers, test results, photos of the equipment or heat pump, and invoices. We don’t need or collect patient information when testing medical equipment.</li>
  <li><strong>When you call, text or email us:</strong> your message and contact details.</li>
  <li><strong>When you enter our giveaway:</strong> your Facebook name and what you post on the giveaway post. If you win, we ask for your contact details and the address of the heat pump to be cleaned.</li>
  <li><strong>When you visit our website:</strong> basic technical information such as your IP address, browser type and the pages you visit, which our hosting provider uses to keep the site running and secure.</li>
</ul>
<p>You don’t have to give us your details, but without a phone number or email we can’t reply to you, and without a site address we can’t do the job.</p>
<h2>Information we get from other people</h2>
<p>Sometimes we get your details from someone else, such as your employer or site manager when they book test &amp; tag, a landlord or property manager who books a heat pump clean and gives us a tenant’s contact for access, a person who refers you to us, or Facebook when you enter our giveaway. We only use these details to arrange and do the job, or to run the giveaway. When we contact you, we’ll tell you who we are and why we have your details, unless you already know.</p>
<h2>How we use it</h2>
<ul>
  <li>To reply to you, quote, book and carry out the job.</li>
  <li>To prepare test &amp; tag registers and remind you when retests are due.</li>
  <li>To invoice you and keep business and tax records.</li>
  <li>To run the giveaway and contact the winner.</li>
  <li>To keep our website working and secure, and, if we advertise, to see which ads lead to enquiries.</li>
</ul>
<p>We won’t send you marketing emails or texts unless you’ve agreed to them, and every marketing message will let you unsubscribe.</p>
<h2>Who we share it with</h2>
<p>We never sell your personal information. We only share it when we need to:</p>
<ul>
  <li><strong>Partner technicians</strong> who carry out test &amp; tag jobs for us outside the Wellington region. They get only what they need to do your job, such as the site address, contact person and equipment details.</li>
  <li><strong>Partners we arrange work through</strong>, such as a registered electrician for new electrical installations, or a specialist who refills and pressure tests fire extinguishers. They also get only what they need to do the work.</li>
  <li><strong>Service providers</strong> who help us run the business: our email provider (Google), our website host (Cloudflare), our website form provider (Formspree), our font provider (Fontshare), and our accountant. If we advertise on Google, Google also receives information about ad clicks, as explained below.</li>
  <li><strong>Meta (Facebook)</strong>, which runs the platform our giveaway takes place on.</li>
  <li>Anyone we’re required to share it with by law.</li>
</ul>
<h2>Information stored overseas</h2>
<p>Some of our service providers store information outside New Zealand, mainly in the United States. We use well-known providers with strong security, and we only use them to store and process information for us, not for their own purposes.</p>
<h2>Cookies and advertising</h2>
<p>Our website doesn’t use cookies to track you. If we advertise on Google, our website may use Google’s advertising tag. It sets cookies that tell us when someone who clicked one of our ads sends a quote request or taps to call us, so we know which ads are useful. It doesn’t give us your name or contact details. You can manage Google ad settings at <a href="https://myadcenter.google.com/" rel="noopener">myadcenter.google.com</a>.</p>
<h2>How we keep it safe</h2>
<p>We keep personal information in password-protected accounts, limit who can see it, and only keep it as long as we need it. Job and invoice records are kept for at least 7 years, because New Zealand tax law requires it. Quote enquiries that don’t go ahead are deleted when we no longer need them.</p>
<p>If a privacy breach happens that is likely to cause serious harm, we’ll tell the people affected and the Privacy Commissioner as soon as we can.</p>
<h2>Your rights</h2>
<p>You can ask to see the personal information we hold about you, and ask us to correct it if it’s wrong. Contact us at {contact}. We’ll respond within 20 working days and won’t charge you to see your information.</p>
<p>If you’re not happy with how we’ve handled your information, please tell us first so we can put it right. You can also complain to the Office of the Privacy Commissioner at <a href="https://www.privacy.org.nz" rel="noopener">privacy.org.nz</a> or 0800 803 909.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The date at the top shows when it last changed.</p>""")
    simple("/terms/", "Terms of Use | Midha Limited", "Terms for using the Midha Limited website, our quotes and prices, the mould-free guarantee, test results and work done by our partners.", "Website terms",
           f"""<p class="note">Last updated {updated}</p>
<p class="lead">These terms apply when you use the Midha Limited website. Please read them along with our <a href="/privacy/">privacy policy</a>.</p>
<h2>Information on this website</h2>
<p>We work hard to keep this website accurate and up to date, but it gives general information only. It isn’t a quote or professional advice for your situation. Contact us for a quote based on your job.</p>
<h2>Prices and quotes</h2>
<ul>
  <li>Prices are in New Zealand dollars and include GST.</li>
  <li>Heat pump cleaning prices are per heat pump.</li>
  <li>A quote is based on the information you give us. If the job turns out to be different from what was described, we’ll talk to you before doing any extra work.</li>
  <li>We may change our prices at any time. A change won’t affect a quote we’ve already given you.</li>
</ul>
<h2>Mould-free guarantee</h2>
<p>The 3-month mould-free guarantee applies to our Comprehensive Clean. If mould comes back on the cleaned heat pump within 3 months of the clean, contact us within that time and we’ll re-clean that heat pump for free.</p>
<h2>Test results</h2>
<p>A test &amp; tag, medical equipment or fire extinguisher check result shows the condition of an item on the day it was tested. It can’t guarantee the item will stay safe afterwards. Between tests, equipment owners should check their gear before use and stop using anything that is damaged. Faults should only be repaired by someone qualified to do so.</p>
<h2>Work done by our partners</h2>
<p>Some work is done by partners we arrange for you: new electrical installations are done by a registered electrician, and fire extinguisher refills and pressure tests are done by a specialist partner. We’ll tell you before any work like this is booked, and include it in your quote.</p>
<h2>Your consumer rights</h2>
<p>Nothing in these terms limits your rights under the Consumer Guarantees Act 1993 or the Fair Trading Act 1986. If you buy our services for business purposes, the Consumer Guarantees Act does not apply, as allowed by section 43 of that Act.</p>
<h2>Our liability</h2>
<p>As far as the law allows, we’re not responsible for indirect loss, such as lost profits or business interruption, that comes from using this website or our services.</p>
<h2>Other websites</h2>
<p>Our website links to other sites, such as Facebook. We don’t control those sites and aren’t responsible for their content or how they handle your information.</p>
<h2>Our content</h2>
<p>The text, photos and logo on this website belong to Midha Limited. Please don’t copy them without our permission.</p>
<h2>New Zealand law</h2>
<p>These terms are governed by New Zealand law.</p>
<h2>Contact</h2>
<p>Questions about these terms? Contact us at {contact}.</p>""")
    simple("/giveaway-terms/", "Giveaway Terms | Win a Free Heat Pump Clean | Midha Limited", "Terms and conditions for the Midha Limited free heat pump clean giveaway, drawn every 3 months for Wellington region residents.", "Giveaway terms and conditions",
           f"""<p class="note">Last updated {giveaway_updated}</p>
<p class="lead">These terms apply to the Midha Limited “Win a free heat pump clean” giveaway. By entering, you agree to them.</p>
<h2>Promoter</h2>
<p>The promoter is Midha Limited, Wainuiomata, Lower Hutt. Contact {contact}.</p>
<h2>The prize</h2>
<ul>
  <li>Each draw has one prize: a free Pro Clean (valued at $79 including GST) for one heat pump at a home in the Wellington region.</li>
  <li>The prize can’t be exchanged for cash or transferred to someone else.</li>
  <li>The Pro Clean must be booked within 3 months of the draw, at a time that suits both the winner and Midha Limited.</li>
</ul>
<h2>Who can enter</h2>
<ul>
  <li>You must be 18 or older and live in the Wellington region, with a heat pump at your home in the region.</li>
  <li>Midha Limited staff, partner technicians and their immediate families can’t enter.</li>
  <li>One entry per person per draw.</li>
</ul>
<h2>How to enter</h2>
<p>Entry is free and you don’t need to buy anything. To enter, follow the steps in our giveaway post on Facebook during the draw period.</p>
<h2>Draw periods and draws</h2>
<ul>
  <li>The giveaway runs in 3-month periods ending on 31 March, 30 June, 30 September and 31 December.</li>
  <li>The winner for each period is drawn at random from all valid entries received during that period. The draw takes place within 5 working days after the period ends.</li>
  <li>Entries don’t carry over to the next period.</li>
</ul>
<h2>Winners</h2>
<ul>
  <li>We’ll contact the winner through Facebook. If the winner doesn’t reply within 7 days, or isn’t eligible, we’ll draw another winner.</li>
  <li>With the winner’s permission, we may share their first name and suburb on our website or Facebook page.</li>
</ul>
<h2>Your information</h2>
<p>We only use entrants’ information to run the giveaway and contact the winner. See our <a href="/privacy/">privacy policy</a>.</p>
<h2>Other terms</h2>
<ul>
  <li>We may disqualify entries that break these terms or that we reasonably believe are fake or fraudulent.</li>
  <li>If something outside our control means we can’t run a draw fairly, we may cancel or change that draw and will announce it on our Facebook page.</li>
  <li>This giveaway is not sponsored, endorsed or run by Facebook or Meta, and is in no way associated with them. By entering, you release Facebook and Meta from any responsibility for it.</li>
</ul>""")
    simple("/404.html", "Page not found | Midha Limited", "Page not found.", "Sorry, we can’t find that page.",
           f'<p class="lead">Try one of these instead:</p><ul class="chips"><li><a href="/heat-pump-cleaning/">Heat pump cleaning</a></li><li><a href="/test-and-tag/">Test &amp; tag</a></li><li><a href="{MED_PATH}">Medical equipment testing</a></li><li><a href="{FIRE_PATH}">Fire extinguisher checks</a></li><li><a href="/electrical-services/">Electrical services</a></li><li><a href="/contact/">Contact</a></li></ul>', robots="noindex")

def cloudflare_files():
    with open(os.path.join(OUT, "_headers"), "w") as f:
        f.write("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/assets/css/*
  Cache-Control: public, max-age=86400

/assets/js/*
  Cache-Control: public, max-age=86400
""")
    with open(os.path.join(OUT, "_redirects"), "w") as f:
        f.write("""# Old page addresses -> new pages (301 = permanent)
/services            /heat-pump-cleaning/   301
/services/           /heat-pump-cleaning/   301
/heat-pump           /heat-pump-cleaning/   301
/heat-pumps          /heat-pump-cleaning/   301
/test-tag            /test-and-tag/         301
/test-and-tag-nz     /test-and-tag/         301
/locations           /test-and-tag/#locations 302
/medical-test-and-tag      /test-and-tag/medical-equipment-testing/  301
/medical-testing           /test-and-tag/medical-equipment-testing/  301
/fire-extinguishers        /test-and-tag/fire-extinguisher-testing/  301
/fire-extinguisher-testing /test-and-tag/fire-extinguisher-testing/  301
/electrical          /electrical-services/  301
/about-us            /about/                301
/contact-us          /contact/              301
/book                /contact/#quote        302
""")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /thanks/\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = (["/", "/test-and-tag/", MED_PATH, FIRE_PATH] + [f"/test-and-tag/{c['slug']}/" for c in CITIES] + [f"/test-and-tag/{RURAL[0]}/"]
            + ["/heat-pump-cleaning/", "/electrical-services/", "/service-areas/", "/reviews/", "/about/", "/contact/", "/privacy/", "/terms/", "/giveaway-terms/"])
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
        json.dump({"name": "Midha Limited", "short_name": "Midha", "start_url": "/", "display": "browser",
                   "background_color": "#FDFCF8", "theme_color": "#FDFCF8",
                   "icons": [{"src": "/assets/img/logo-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/assets/img/logo-512.png", "sizes": "512x512", "type": "image/png"}]}, f, indent=2)

if __name__ == "__main__":
    home(); heat_pump(); test_tag(); medical_page(); fire_page(); [city_page(c) for c in CITIES]; rural_page(); electrical(); areas_page(); reviews_page(); about_page(); contact_page(); misc(); cloudflare_files()
    print("built", OUT)
