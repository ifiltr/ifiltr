"""
    iFiltr, Simple & Secure Social Shopping.
    Copyright (C) 2012-2013 iFiltr (<https://ifiltr.com>).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ifiltr.dev_settings'
from ifiltr_site.models import Category

if __name__ == '__main__':
  mainCategories = {'Appliances':{},
                    'Art':{},
                    'Baby':{},
                    'Books':{},
                    'Classifieds':{},
                    'Collectibles & Memorabilia':{},
                    'Computers & Tablets':{},
                    'Crafts':{},
                    'Electronics':{},
                    'Fashion':{},
                    'Furniture':{},
                    'Gifts Cards, Coupons, & Deals':{},
                    'Grocery':{},
                    'Holiday & Seasonal':{},
                    'Home & Garden':{},
                    'Motors/Vehicles/Boats':{},
                    'Movies':{},
                    'Music':{},
                    'Outdoor':{},
                    'Pet':{},
										'Real Estate':{},
										'Sporting Goods':{},
										'Stamps':{},
										'Tickets':{},
										'Tools & Hardware':{},
										'Toys, Games, Hobbies':{},
										'Travel':{},
                    'Other/Everything Else':{}}

  mainCategories['Appliances'] = {'Cooking':{},
								 'Cookware':{},
								 'Countertop Appliances':{},
								 'Dishwashing':{},
								 'Freezers':{},
								 'Laundry':{},
								 'Outdoor Grills':{},
								 'Refrigeration':{},
								 'Seasonal':{},
								 'Vacuums & Carpet Cleaning':{}}
							  
  mainCategories['Art'] = {'Directly from Artist':{},
						  'From Dealers & Resellers':{},
						  'Wholesale':{}}
						  
  mainCategories['Baby'] = {'Accessories':{},
						   'Bathing & Skincare':{},
						   'Bedding':{},
						   'Car Seats':{},
						   'Cribs':{},
						   'Decor':{},
						   'Diapering':{},
						   'Furniture':{},
						   'Gear':{},
						   'Healthy':{},
						   'Safety':{},
						   'Strollers':{},
						   'Toddler':{},
						   'Toys':{},
						   'Wholesale':{}}
						
  mainCategories['Books'] = {'Accessories':{},
							'Antique & Collectible':{},
							'Audiobooks':{},
							'Catalogs':{},
							'Childrens Books':{},
							'Cookbooks':{},
							'eBooks':{},
							'Magazines':{},
							'Preorder':{},
							'Songbooks':{},
							'Textbooks, Education':{},
							'Wholesale & Bulk':{}}
							
  mainCategories['Classifieds'] = {}
  
  mainCategories['Collectibles & Memorabilia'] = {'Apparel':{},
												 'Autographs - Original':{},
												 'Autographs - Reprints':{},
												 'Cards':{},
												 'Movies':{},
												 'Music':{},
												 'Sports':{},
												 'Souvenirs':{},
												 'Television':{},
												 'Theater':{},
												 'Video Game':{}}
												 
  mainCategories['Computers & Tablets'] = {'Cables & Connectors':{},
										  'Computer Components & Parts':{},
										  'Computer Games':{},
										  'Desktops & All-In-Ones':{},
										  'Drives, Storage & Blank Media':{},
										  'Enterprise Networking, Servers':{},
										  'Gadgets':{},
										  'Home Networking & Connectivity':{},
										  'iPad, Tablet & eBook Accessories':{},
										  'iPads, Tablets & eBooks':{},
										  'Keyboards, Mice & Pointing':{},
										  'Laptop, Notebook & Desktop Accessories':{},
										  'Laptops & Netbooks':{},
										  'Manuals & Resources':{},
										  'Monitors & Projectors':{},
										  'Power Projection, Distribution':{},
										  'Printer, Scanner & Fax Supplies':{},
										  'Printers, Scanners & Fax Machines':{},
										  'Software':{},
										  'Vintage Computing':{},
										  'Wholesale':{}}
										  
  mainCategories['Crafts'] = {'Art Supplies':{},
							 'Beads & Jewelry Making':{},
							 'Glass & Mosaics':{},
							 'Handcrafted & Finished Pieces':{},
							 'Home Arts & Crafts':{},
							 'Kids Crafts':{},
							 'Multi-Purpose Craft Supplies':{},
							 'Needlecraft & Yarn':{},
							 'Scrapbooking & Paper Crafts':{},
							 'Sewing & Fabric':{},
							 'Stamping & Embossing':{},
							 'Wholesale':{},
							 'Other Crafts':{}}
							 
  mainCategories['Electronics'] = {'Accessories':{},
								  'Camera, Photo & Video':{},
								  'Car Electronics & GPS':{},
								  'Cell Phones & Accessories':{},
								  'Computers & Tablets':{},
								  'Home Audio & Theater':{},
								  'Home Automation':{},
								  'Home Surveillance':{},
								  'Home Telephones':{},
								  'Multipurpose Batteries & Power':{},
								  'Musical Instruments':{},
								  'Portable Audio & Headphones':{},
								  'Radio Communication':{},
								  'Video Games & Consoles':{},
								  'Vintage Electronics':{},
								  'Wholesale':{}}
								  
  mainCategories['Fashion'] = {'Accessories':{},
                              'Activewear':{},
                              'Casual':{},
                              'Clearance':{},
                              'Cold Weather':{},
                              'Costume':{},
                              'Cultural and Ethnic':{},
                              'Dress':{},
                              'Eyewear':{},
                              'Gear':{},
                              'Hair and Body':{},
                              'Handbags and Wallets':{},
                              'Hats':{},
                              'Health and Beauty':{},
                              'Hoodies':{},
                              'Jackets':{},
                              'Jewelry':{},
                              'Lingerie':{},
                              'Long Sleeve':{},
                              'Maternity':{},
                              'Merchendise':{},
                              'Nightwear':{},
                              'Outerwear':{},
                              'Pants':{},
                              'Plus Size':{},
                              'Polos':{},
                              'Shoes':{},
                              'Shorts':{},
                              'Skirt':{},
                              'Shirts':{},
                              'Socks':{},
                              'Sports':{},
                              'Sweaters':{},
                              'Swim':{},
                              'Travel':{},
                              'Underwear':{},
                              'Unisex':{},
                              'Vests':{},
                              'Vintage':{},
                              'Warm Weather':{},
                              'Wedding and Formal':{},
                              'Other':{}}
							  
  mainCategories['Furniture'] = {'Accessories & Gifts':{},
								'Bedroom sets':{},
								'Dining Room Sets':{},
								'Entertainment Centers & TV Stands':{},
								'Fireplaces':{},
								'Home Office':{},
								'Kids Furniture':{},
								'Mattress Sets':{},
								'Mattresses':{},
								'Occasional Tables':{},
								'Ottomans & Accent Chairs':{},
								'Reclaimed & Rustic':{},
								'Recliners':{},
								'Sofas & Sectionals':{}}
								
  mainCategories['Gifts Cards, Coupons, & Deals'] = {'Coupons':{},
													'Deal Vouches':{},
													'Gift Cards':{},
													'Gift Certificates':{},
													'Law Enforcement Deals':{},
													'Military & Government Deals':{}}
													
  mainCategories['Grocery'] = {'Alcoholic Beverages':{},
							  'Baby Food':{},
							  'Breakfast & Cereal Bars':{},
							  'Baking':{},
							  'Batteries':{},
							  'Beverages':{},
							  'Boxed Meals':{},
							  'Breakfast & Cereal':{},
							  'Candy, Gum & Mints':{},
							  'Canned Goods & Soups':{},
							  'Chocolate':{},
							  'Coffee':{},
							  'Condiments, Sauces & Spices':{},
							  'Fresh Flowers':{},
							  'Fresh Food':{},
							  'Gluten-Free':{},
							  'Gourmet Gifts':{},
							  'Grocery & Gourmet Food':{},
							  'Herbs, Spices & Seasoning':{},
							  'Household Essentials':{},
							  'Infant & Childcare':{},
							  'International Food':{},
							  'Meal Solutions, Grains & Pasta':{},
							  'Natural & Organic':{},
							  'Snacks, Cookies & Chips':{},
							  'Tea':{},
							  'Vegan':{},
							  'Vegetarian':{}}
							
  mainCategories['Holiday & Seasonal'] = {'Anniversary':{},
										 'April Fools Day':{},
										 'Armed Forces Day':{},
										 'Birthday':{},
										 'Chinese New Year':{},
										 'Christmas':{},
										 'Columbus Day':{},
										 'Easter':{},
										 'Fathers Day':{},
										 'Halloween':{},
										 'Hanukkah':{},
										 'Independence Day / Fourth of July':{},
										 'Kwanzaa':{},
										 'Labor Day':{},
										 'Mardi Gras':{},
										 'Martin Luther King Day':{},
										 'Memorial Day':{},
										 'Mothers Day':{},
										 'New years':{},
										 'Presidents Day':{},
										 'St. Patricks day':{},
										 'Thanksgiving':{},
										 'Valentines Day':{},
										 'Veterans Day':{}}
										 
  mainCategories['Home & Garden'] = {'Bath':{},
									'Bedding':{},
									'Building materials':{},
									'Composters & Accessories':{},
									'Electrical':{},
									'Fertilizer & Weed Control':{},
									'Food & Wine':{},
									'Flooring':{},
									'Fountains & Ponds':{},
									'Furniture':{},
									'Garden Arbors & Trellises':{},
									'Garden Hoses & Accessories':{},
									'Garden Insect & Pest Control':{},
									'Garden Tools':{},
									'Greenhouses':{},
									'Hardware':{},
									'Heating & Cooling':{},
									'Holidays, Cards & Party Supplies':{},
									'Housekeeping, Cleaning & Organization':{},
									'Interior & Exterior Paint':{},
									'Kids & Teens':{},
									'Kitchen, Dining & Bar':{},
									'Lamps, Lighting & Ceiling Fans':{},
									'Lawncare & Landscaping':{},
									'Home Decor':{},
									'Home Improvement':{},
									'Lumber & Composites':{},
									'Outdoor Decor':{},
									'Plants':{},
									'Plant Stands & Accessories':{},
									'Plant Supplies':{},
									'Plumbing':{},
									'Rugs & Cultivators':{},
									'Soil':{},
									'Tillers & Cultivators':{},
									'Tools':{},
									'Wedding Supplies':{},
									'Wheelbarrows & Carts':{},
									'Windows & Doors':{},
									'Window Treatment & Hardware':{},
									'Yard, Garden & Outdoor':{},
									'Wholesale':{}}
									
  mainCategories['Motors/Vehicles/Boats'] = {'Boats':{},
											'Car Care & Maintenance':{},
											'Cars & Trucks':{},
											'Exterior Accessories':{},
											'Insurance':{},
											'Interior Accessories':{},
											'Lights':{},
											'Motorcycles':{},
											'Parts & Accessories':{},
											'Powersports':{},
											'Tires':{},
											'Wheels':{}}
											
  mainCategories['Movies'] = {'Blu-Ray':{},
							 'Movies (DVD)':{},
							 'New Releases (Blu-Ray & DVD)':{},
							 'Pre-Order (Blu-Ray & DVD)':{},
							 'TV Shows (DVD)':{}}
							 
  mainCategories['Music'] = {'Cassettes':{},
							'CDs':{},
							'Digital Audio':{},
							'Equipment':{},
							'Instruction Books, CDs & Video':{},
							'Instruments':{},
							'MP3 Downloads':{},
							'Music':{},
							'Other Music Formats':{},
							'Preorder':{},
							'Records':{},
							'Sheet Music & Songbooks':{},
							'Storage & Media Accessories':{},
							'Wholesale':{}}

  mainCategories['Outdoor'] = {'Airguns, Airsoft & Paintball':{},
							  'Animal & Pet Care':{},
							  'Bikes':{},
							  'Building materials':{},
							  'Camping & Hiking':{},
							  'Canopies, Gazebos & Shade':{},
							  'Decking':{},
							  'Exterior Paint':{},
							  'Fencing':{},
							  'Games':{},
							  'Grills & Accessories':{},
							  'Hot Tub & Saunas':{},
							  'Hunting, Fishing & Shooting':{},
							  'Firepits & Outdoor Heating':{},
							  'Lawncare & Landscaping':{},
							  'Lumber & Composites':{},
							  'Mowers & Tractors':{},
							  'Outdoor Decor':{},
							  'Outdoor Lighting':{},
							  'Outdoor Play - Trampolines':{},
							  'Outdoor Power Equipment & Parts':{},
							  'Outdoor Recreation':{},
							  'Paddle & Water':{},
							  'Patio Furniture':{},
							  'Planters & Window Boxes':{},
							  'Playsets & Swingsets':{},
							  'Pools & Pool Care':{},
							  'Scooters & Ride-Ons':{},
							  'Sheds, Garages & Outdoor Storage':{},
							  'Skateboarding':{},
							  'Winter Sports':{}}
							  
  mainCategories['Pet'] = {'Bird':{},
						  'Cat':{},
						  'Dog':{},
						  'Ferret':{},
						  'Fish':{},
						  'Flea & Tick':{},
						  'Horse':{},
						  'Reptile':{},
						  'Small Pet':{},
						  'Other':{},
						  'Wholesale':{}}
						  
  mainCategories['Real Estate'] = {'For Rent':{},
								  'For Sale':{}}
								  
  mainCategories['Sporting Goods'] = {'Camping':{},
									 'Cycling':{},
									 'Exercise & Fitness':{},
									 'Fan Shop':{},
									 'Game Room':{},
									 'Gymnastics':{},
									 'Golf':{},
									 'Hunting, Fishing & Shooting':{},
									 'Indoor Games':{},
									 'Outdoor Games':{},
									 'Skateboarding':{},
									 'Team Sports':{},
									 'Tennis & Racquet':{},
									 'Water Sports & Boating':{},
									 'Winter Sports':{},
									 'Wholesale':{}}
									 
  mainCategories['Stamps'] = {'Publications':{},
							 'Specialty & Topical':{},
							 'Supplies':{},
							 'United State':{},
							 'Worldwide':{}}
							 
  mainCategories['Tickets'] = {'Concerts':{},
							  'Sports':{},
							  'Theaters':{}}
							  
  mainCategories['Tools & Hardware'] = {'Air Compressors & Air Tools':{},
									   'Automotive Tools':{},
									   'Generators':{},
									   'Hand Tools':{},
									   'Hardware':{},
									   'Power Tool Accessories':{},
									   'Power Tools':{},
									   'Safety & Security':{},
									   'Tool Storage & Workbenches':{},
									   'Wet/Dry Vacuums':{},
									   'Workwear & Safety Gear':{}}
									   
  mainCategories['Toys, Games, Hobbies'] = {'Action Figures':{},
										   'Beanbag Plush':{},
										   'Bikes & Riding Toys':{},
										   'Building Toys':{},
										   'Classic Toys':{},
										   'Development & Learning Toys':{},
										   'Diecast & Toy Vehicles':{},
										   'Dolls & Dollhouses':{},
										   'Education':{},
										   'Electronic, Battery & Wind-Up':{},
										   'Fast Food & Cereal Premiums':{},
										   'Games':{},
										   'Kids Electronics':{},
										   'Marbles':{},
										   'Model Railroads & Trains':{},
										   'Models & Kits':{},
										   'Music Instruments & Karaoke':{},
										   'Outdoor Toys & Structures':{},
										   'Pretend Play & Preschool':{},
										   'Puzzles':{},
										   'Remote Control & Control Line':{},
										   'Robots':{},
										   'Monster Toys':{},
										   'Space Toys':{},
										   'Slot Cars':{},
										   'Stuffed Animals':{},
										   'Toy Soldiers':{},
										   'Trading Card Games':{},
										   'TV, Movie & Character Toys':{},
										   'Vintage & Antique Toys':{},
										   'Wholesale':{}}
										   
  mainCategories['Travel'] = {'Airline':{},
							 'Campground & RV Parks':{},
							 'Car Rental':{},
							 'Cruises':{},
							 'Lodging':{},
							 'Luggage':{},
							 'Luggage Accessories':{},
							 'Maps':{},
							 'Rail':{},
							 'Travel Accessories':{},
							 'Vacation Packages':{}}
							 
  mainCategories['Other/Everything Else'] = {'Adult Only':{},
											'Advertising Opportunities':{},
											'Career Development & Education':{},
											'Credit Cards':{},
											'For Businesses':{},
											'Funeral & Cemetery':{},
											'Genealogy':{},
											'Information Products':{},
											'Memberships':{},
											'Metaphysical':{},
											'Personal Development':{},
											'Personal Security':{},
											'Religious Products & Supplies':{},
											'Special Promotions':{},
											'Weird Stuff':{}}

  mainCategories['Pet']['Bird'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Cat'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Dog'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Ferret'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Fish'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Flea & Tick'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Horse'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Reptile'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Small Pet'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Other'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Pet']['Wholesale'] = {'Food & Health':{},
								 'Supplies & Training':{},
								 'Other':{}}
								 
  mainCategories['Real Estate']['For Rent'] = ['2-Story [Single Family Home]',
											  'Apartment',
											  'Commercial',
											  'Condo',
											  'Coop',
											  'Duplex',
											  'Foreclosure',
											  'Houseboat',
											  'Income/Investment',
											  'Loft',
											  'Lot/Land',
											  'Mobile/Manufactured',
											  'Multi-Family Home',
											  'New Home',
											  'Ranch [Single Family Home]',
											  'Resort',
											  'Studio',
											  'TIC',
											  'Timeshare',
											  'Townhome',]
											  
  mainCategories['Real Estate']['For Sale'] = {'2-Story [Single Family Home]':{},
											  'Apartment':{},
											  'Commercial':{},
											  'Condo':{},
											  'Coop':{},
											  'Duplex':{},
											  'Foreclosure':{},
											  'Houseboat':{},
											  'Income/Investment':{},
											  'Loft':{},
											  'Lot/Land':{},
											  'Mobile/Manufactured':{},
											  'Multi-Family Home':{},
											  'New Home':{},
											  'Ranch [Single Family Home]':{},
											  'Resort':{},
											  'Studio':{},
											  'TIC':{},
											  'Timeshare':{},
											  'Townhome':{}}
  
  mainCategories['Fashion']['Shirts'] = [
    'Size',
    'Style',
    'Color',
    'Brand',
    'Minimum Price',
    'Max Price',
    'Sleeve Length'
  ]

  print 'deleting errthang'
  Category.objects.all().delete()

  print mainCategories.keys()
  for mainCat in mainCategories.keys():
    thisCat = Category(parent=None, name=mainCat, depth = 0)
    thisCat.save()
    print 'adding ', mainCat
    for subCat in mainCategories[mainCat].keys():
      thisSubCat = Category(parent=thisCat, name=subCat, depth = 1)
      thisSubCat.save()
      for filt in mainCategories[mainCat][subCat]:
        thisfilt = Category(parent=thisSubCat, name=filt, depth = 2)
        thisfilt.save()
