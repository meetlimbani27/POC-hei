import pandas as pd

# Creating a new DataFrame with the generated data
new_data = [
    ["Golden Grain Distributors", "Richard Morgan", "Barley", "Supplier of premium barley, providing high-quality grains for breweries.", "9123456789", "richard@goldengrain.com"],
    ["Fresh Hops Co.", "Sarah Johnson", "Hops", "Family-owned hop farm offering a range of hop varieties for craft brewers.", "9234567890", "sarah@freshhops.com"],
    ["CleanWater Solutions", "Thomas Kelly", "Water Filtration", "Specializing in water filtration systems for breweries, ensuring pure water quality.", "9345678901", "thomas@cleanwater.com"],
    ["BrewMalt Ltd.", "Emma Davis", "Malt", "Suppliers of malted barley and grains to craft breweries across the region.", "9456789012", "emma@brewmalt.com"],
    ["FermentTech Inc.", "James Turner", "Fermentation Equipment", "Manufacturer of advanced fermentation tanks and brewing vessels.", "9567890123", "james@fermenttech.com"],
    ["YeastMasters", "Lily Moore", "Yeast", "Providing high-quality brewing yeast for various beer styles.", "9678901234", "lily@yeastmasters.com"],
    ["BrewLuxe Packaging", "Peter Harris", "Packaging", "Supplier of custom glass bottles and packaging for craft beers.", "9789012345", "peter@brewluxepackaging.com"],
    ["CraftCans Ltd.", "George Clark", "Canning", "Specializing in aluminum cans for craft breweries, including custom designs.", "9890123456", "george@craftcans.com"],
    ["BrewTech Automation", "Natalie Adams", "Brewing Equipment", "Providing automated brewing systems for breweries to improve efficiency.", "9901234567", "natalie@brewtech.com"],
    ["The Hoppy Barrel", "Mark Robinson", "Hops", "Supplier of organic hops from family farms for craft brewers.", "9012345678", "mark@thehoppybarrel.com"],
    ["PureBarley Mills", "Olivia Harris", "Barley", "Leading supplier of malted barley and grains for large breweries.", "9123456789", "olivia@purebarleymills.com"],
    ["EcoBrew Filters", "Benjamin Scott", "Filtration", "Providing eco-friendly water filtration systems for breweries.", "9234567890", "benjamin@ecobrewfilters.com"],
    ["BrewMaster's Tools", "Ethan Lewis", "Brewing Tools", "Suppliers of premium brewing tools and gadgets for craft brewers.", "9345678901", "ethan@brewmasterstools.com"],
    ["HopKing Farms", "Sophia Wright", "Hops", "Organic hop supplier known for high-quality hops for boutique breweries.", "9456789012", "sophia@hopkingfarms.com"],
    ["GoldenKeg Co.", "Henry Turner", "Kegs", "High-quality stainless steel kegs and kegging systems for breweries.", "9567890123", "henry@goldenkeg.com"],
    ["HopsFresh Ltd.", "Lucas King", "Hops", "Supplier of freshly harvested hops for crafting unique beer flavors.", "9678901234", "lucas@hopsfresh.com"],
    ["BrewTec Systems", "Grace Evans", "Brewing Equipment", "Offering a variety of advanced brewing systems for larger production batches.", "9789012345", "grace@brewtec.com"],
    ["FermentEase", "Oliver Thompson", "Fermentation", "Specializing in yeast fermentation services to enhance beer flavor and consistency.", "9890123456", "oliver@fermentease.com"],
    ["MaltyGrain Co.", "Sophie Carter", "Malt", "Supplier of both raw and roasted malts, tailored for craft brewers.", "9901234567", "sophie@maltygrain.com"],
    ["GreenBrewers", "Samuel Allen", "Sustainable Brewing", "Providing sustainable brewing solutions, including energy-saving equipment.", "9012345678", "samuel@greenbrewers.com"],
    ["Brewspring", "Ava Wright", "Equipment", "Leading manufacturer of advanced brewing equipment for efficient production.", "9123456789", "ava@brewspring.com"],
    ["HopWise Inc.", "Zachary White", "Hops", "Hop supplier providing a variety of strains to enhance the flavor profile of beers.", "9234567890", "zachary@hopwise.com"],
    ["Silver Oak Brewing Supplies", "Liam Jackson", "Brewing Supplies", "Supplying everything from brewing kits to premium ingredients for craft brewers.", "9345678901", "liam@silveroakbrew.com"],
    ["CraftBeerCans", "Isabella Young", "Packaging", "Packaging service offering custom cans and bottles for craft beer.", "9456789012", "isabella@craftbeercans.com"],
    ["YeastFlow", "Michael Walker", "Yeast", "Specializing in high-performance yeasts for breweries to create distinct flavors.", "9567890123", "michael@yeastflow.com"],
    ["The Brew Exchange", "Ethan Carter", "Brew Supplies", "Brew supply company offering everything a brewery needs for production and packaging.", "9678901234", "ethan@thebrewexchange.com"],
    ["StoutLuxe", "Amelia Harris", "Malt", "Supplier of specialty malts for creating rich, robust stout beers.", "9789012345", "amelia@stoutluxe.com"],
    ["BeerTech Industries", "Jack Moore", "Brewing Equipment", "Providing cutting-edge brewing equipment designed for craft beer efficiency.", "9890123456", "jack@beertechindustries.com"],
    ["Golden Hops Ltd.", "Noah Taylor", "Hops", "Supplier of gold-standard hops for brewing the finest craft beers.", "9901234567", "noah@goldenhops.com"],
    ["Brewers' Edge", "Charlotte King", "Brewing Tools", "Specializing in tools and equipment designed for home and microbreweries.", "9012345678", "charlotte@brewersedge.com"],
    ["MicroMalt Co.", "Mason Scott", "Malt", "Micro-malt supply company providing specialty malts for smaller batch breweries.", "9123456789", "mason@micromalt.com"],
    ["AleCraft Supply", "Amos Brown", "Yeast", "Supplier of craft ale-specific yeast strains for unique beer creations.", "9234567890", "amos@alecraft.com"],
    ["The Beer Factory", "Harper Garcia", "Brewing Supplies", "Offering a comprehensive range of supplies, ingredients, and equipment for breweries.", "9345678901", "harper@thebeerfactory.com"],
    ["CanningMasters", "Jaxon Harris", "Canning", "Provider of high-end canning lines for breweries to package their beers with precision.", "9456789012", "jaxon@canningmasters.com"],
    ["EcoHop Enterprises", "Ella Martinez", "Hops", "Eco-friendly hop farm known for sustainable farming and hop production.", "9567890123", "ella@ecohop.com"],
    ["CraftWort Brewing", "Lily Anderson", "Brewing Supplies", "Providing wort, malt extracts, and other brewing essentials to craft breweries.", "9678901234", "lily@craftwortbrewing.com"],
    ["HopCrafters", "Benjamin Lewis", "Hops", "Supplier of rare hop varieties, providing unique flavors for craft brewers.", "9789012345", "benjamin@hopcrafters.com"],
    ["YeastSource", "Madeline Clark", "Yeast", "One-stop shop for premium, specialized yeast strains for various beer types.", "9890123456", "madeline@yeastsource.com"],
    ["BrewBlend", "Oliver Green", "Malt", "Producer of unique malt blends for breweries looking to create new beer styles.", "9901234567", "oliver@brewblend.com"],
    ["BarleyHouse", "Ella Moore", "Barley", "Supplier of high-quality, locally sourced barley for small and large breweries.", "9012345678", "ella@barleyhouse.com"],
    ["Hops & Co.", "Gabriel White", "Hops", "Sourcing hops from local farms to provide a fresh and organic selection for breweries.", "9123456789", "gabriel@hopsandco.com"],
    ["BrewCo Machines", "Sophia Taylor", "Brewing Equipment", "Designing and manufacturing machinery tailored for the craft brewing industry.", "9234567890", "sophia@brewcomachines.com"],
    ["BeerWell", "Lucas Moore", "Brewing Supplies", "Offering brewing systems, ingredient kits, and equipment to breweries worldwide.", "9345678901", "lucas@beerwell.com"],
    ["Brewtech Systems", "Olivia Harris", "Brewing Equipment", "Designs and sells brewing systems for small-scale breweries.", "9456789012", "olivia@brewtechsystems.com"],
    ["HopHarvester", "Charlotte King", "Hops", "Harvesting and selling premium hops directly from farms to breweries.", "9567890123", "charlotte@hopharvester.com"],
    ["GoldenHops Enterprises", "William Turner", "Hops", "Specializing in high-quality, handpicked hops for local and international breweries.", "9678901234", "william@goldenhops.com"],
    ["HopLabs", "Madeline Young", "Hops", "Research-focused hop supplier dedicated to improving hop quality and yield.", "9789012345", "madeline@hoplabs.com"],
    ["MaltBrewers", "Grace Walker", "Malt", "Specializing in malted barley and specialty malts for craft breweries.", "9890123456", "grace@maltbrewers.com"],
    ["BrewMalt Supplies", "Mason Turner", "Malt", "Supplier of both base and specialty malts for brewing diverse beer styles.", "9901234567", "mason@brewmaltsupplies.com"],
    ["HopHarvesters", "Isabella Martin", "Hops", "Local hop farm with a focus on sustainable growing practices and unique hop varieties.", "9012345678", "isabella@hopharvesters.com"],
    ["BrewForAll", "Jackson Walker", "Brewing Equipment", "Global provider of brewing equipment and technology solutions for all sizes of breweries.", "9123456789", "jackson@brewforall.com"],
    ["Fermenting Innovations", "Amos Scott", "Fermentation", "Innovative fermentation systems that optimize the brewing process for higher yield.", "9234567890", "amos@fermentinginnovations.com"]
]

# Convert new_data to a DataFrame
new_df = pd.DataFrame(new_data, columns=["Vendor company name", "Vendor name", "Industry", "Description", "Contact number", "Email id"])

# Saving the new data to an Excel file
new_file_path = "Generated_Vendor_Data.xlsx"
new_df.to_excel(new_file_path, index=False)

print(f"Data saved to {new_file_path}")
