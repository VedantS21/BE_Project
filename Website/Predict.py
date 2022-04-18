import pandas as pd
from io import BytesIO

from PIL import Image
import streamlit as st
import model

def doc_nearby(city):
    abc = "https://www.practo.com/"+ city + "/dermatologist"
    st.text(abc)
    url = abc
   
    st.markdown("check out this [link](%s)" % url)

def app():
    model_path = r"SDModel/Final_TensorFlow"
    tf_model = model.TFModel(model_path)
    tf_model.load()

    st.title("Skin Diseases Detection")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.success("Capture a closer Image of Infected Area in proper lighting condition")
    file = st.file_uploader("", type=["png","jpg","jpeg"])
    show_file = st.empty()

    if not file:
        print("File not selected")
        show_file.info("Please UPLOAD a file : {} ".format(''.join(["png","jpg","jpeg"])))
        return
    content = file.getvalue()

    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        data = pd.read_csv(file)
        st.dataframe(data.head(10))
    file.close()

    result = st.button("Predict", key="b1") 
      

    print(type(file))
    print(type(content))
    image = Image.open(BytesIO(content))
    output = dict()
    
    if result == True:
        output = tf_model.predict(image)
        print(type(output))
        max_conf = 1.0
        final_pred = dict()
        for pred in output["predictions"]:
            print(pred)
            if round(pred["confidence"],4) == max_conf:
                print(type(pred["confidence"]))
                final_pred = pred
                print(type(final_pred))
        try:
            st.subheader("Disease: "+final_pred['label'])
            final_pred = str(final_pred['label'])
            # st.write(final_pred)
            print(final_pred)

            if final_pred == "Eczema" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Moisturize your skin often.
                    2) Avoid sudden changes in temperature or humidity.
                    3) Try not to sweat or get too hot.
                    4) Avoid scratchy materials such as wool.
                    5) Don't use harsh soaps, detergents, or solvents.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) Apply Aloe vera gel
                    2) Bath atleast 2-3 times a day.
                    3) Apply coconut oil.
                    4) Apply honey
                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Fatty fish, You may be able to reduce your symptoms by eating fatty fish, such as salmon and herring.
                    2) Foods containing quercetin like apples, blueberries, cherries, broccoli, spinach, kale.
                    3) Foods containing probiotics like sourdough bread, soft cheeses, such as Gouda, naturally fermented pickles, kefir, 
                    unpasteurized sauerkraut
                    """
                    )
            elif final_pred == "Foot Ulcer" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Proper Footwear, Podiatrists recommend wearing clean, dry socks that don’t have tight elastic bands, which may restrict 
                    blood flow to the foot.
                    2) Controlling blood sugar level, If you have diabetes, you must monitor blood sugar levels and ensure that they are in a healthy 
                    range. High blood sugar may lead to foot complications and difficulty healing.
                    3) Tobacco Cessation, Cigarettes and other tobacco products contain chemicals that slow healing, which may prevent a full recovery 
                    from a foot ulcer. 
                    4) Weight loss, being overweight or obese places increased stress on the feet, which can create friction when wearing shoes and lead 
                    to blisters and cuts.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) Leg elevation. To help blood flow out of your leg, keep your leg above your heart. Prop it up on cushions or pillows.
                    2) Compression socks. Compression socks reduce leg swelling by helping blood flow back up to the heart.
                    3) Saline solution. If you have a mild skin ulcer, you can clean it with sterile salt water called saline. If your ulcer is severe, 
                    a wound-care nurse should do it instead.
                    4) Turmeric. Turmeric has antimicrobial, antioxidant, and anti-inflammatory properties that may help wound healing. To use it, mix a 
                    2-to-1 ratio of ground turmeric and water and gently apply the paste on the sore.
                    5) Honey, traditionally, honey is used for wound healing because it has anti-inflammatory and antimicrobial benefits. To try this 
                    method, apply high-quality honey to a dressing, then apply the dressing on the skin.   
                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Protein-rich foods, including: Lean meats and seafood, Skinless poultry, Eggs, Tofu
                    2) Whole-grain and high-fiber carbohydrates, such as: Whole-grain breads, cereals, and pasta, Brown rice, Beans, 
                    Fruits with the skin, Berries
                    3) Non-starchy vegetables, such as: Cauliflower, Tomatoes, Peppers, Carrots, Broccoli, Cabbage, Kale, Spinach
                    """
                    )
                
                city = st.text_input("Enter Your City")
                doc_nearby(city)
            
            elif final_pred == "measles" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Stay home from work or school and other public places until you aren’t contagious. This is four days after you 
                    first develop the measles rash.
                    2) Avoid contact with people who may be vulnerable to infection, such as infants too young to be vaccinated and 
                    immunocompromised people.
                    3) Cover your nose and mouth if you need to cough or sneeze. Dispose of all used tissues promptly. If you don’t have a 
                    tissue available, sneeze into the crook of your elbow, not into your hand.
                    4) Be sure to wash your hands frequently and to disinfect any surfaces or objects that you touch frequently.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) Take it easy. Get rest and avoid busy activities.
                    2) Sip something. Drink plenty of water, fruit juice and herbal tea to replace fluids lost by fever and sweating.
                    3) Seek respiratory relief. Use a humidifier to relieve a cough and sore throat.
                    4) Rest your eyes. If you or your child finds bright light bothersome, as do many people with measles, keep the 
                    lights low or wear sunglasses. Also avoid reading or watching television if light from a reading lamp or from the 
                    television is bothersome.  
                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Food rich in Vitamin C like Orange, Grapefruit.
                    2) Product rich in Vitamin A like Spinach, Green leafy vegetables.
                    3) Avoiding greasy food; food containing fat and processed items.
                    4) Not consuming caffeinated and sweet drinks like coffee and soft drinks.
                    5) Immunity can be improved by drinking a boiled mixture of – half cup water, little ginger, two-three leaves of sweet 
                    basil(tulsi) and mint leaves.
                    """
                    )
            
            elif final_pred == "ringworm" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Keep your skin clean and dry.
                    2) Wear shoes that allow air to circulate freely around your feet.
                    3) Don’t walk barefoot in areas like locker rooms or public showers.
                    4) Clip your fingernails and toenails short and keep them clean.
                    5) Change your socks and underwear at least once a day.
                    6) Don’t share clothing, towels, sheets, or other personal items with someone who has ringworm.
                    7) Wash your hands with soap and running water after playing with pets. If you suspect that your 
                    pet has ringworm, take it to see a veterinarian. If your pet has ringworm, follow the steps below 
                    to prevent spreading the infection.
                    8) If you’re an athlete involved in close contact sports, shower immediately after your practice session or match, 
                    and keep all of your sports gear and uniform clean. Don’t share sports gear (helmet, etc.) with other players.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) Garlic, To use garlic as a treatment, make a paste of crushed garlic cloves by blending the garlic with some 
                    olive or coconut oil. Apply a thin layer of paste to the affected skin and cover with gauze. Leave in place for up 
                    to 2 hours before rinsing. Repeat twice daily until symptoms resolve.
                    2) Bath 2-3 times a day.
                    3) Apply the gel from an aloe vera plant onto the ringworm patch three or four times daily. The gel also has cooling 
                    properties, so it may soothe itchy and swollen skin.
                    4) You can use coconut oil as a moisturizing lotion, which may be an effective way to prevent future ringworm infections.
                    5) Apply mixture of coconut oil and turmeric and take neem bath.

                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Proteins such as lean meat, eggs and beans.
                    2) Omega-3 sources like nuts, seeds and fatty fish.
                    3) Whole grains such as oatmeal, brown rice and quinoa.
                    4) Leafy Vegetables.
                    5) Yogurt.
                    6) Drink plenty of water.
                    """
                    )
            
            elif final_pred == "Herpes Zoster" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Cover the rash.
                    2) Avoid touching or scratching the rash.
                    3) Wash your hands often.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) You can also take a healing bath to reduce symptoms. Pour 1 to 2 cups of colloidal oatmeal or cornstarch into 
                    lukewarm bathwater and soak for 15 to 20 minutes. Do not use hot water. Hot water can worsen shingles blisters 
                    because heat increases blood flow.
                    2) In addition to taking a bath to relieve pain and itchiness associated with a shingles rash, apply a cool, moist compress.
                    3) Apply lotions and creams sparingly.
                    4) Some supplements and herbal medicines may also help your body fight the virus, and treat insomnia and anxiety 
                    due to shingles. These include: melatonin, oregano oil, Echinacea, lemon balm, green, tea, essential, fatty acids
                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Lightly cooked, fresh, green and yellow vegetables. This would be easier to digest.
                    2) All fresh fruits except citrus fruits.
                    3) Legumes like black-eyed peas, chickpeas, lentils, kidney beans, Mushrooms, etc.
                    4) Consume whole grains, especially millets, but in moderate quantities.
                    """
                    )
            elif final_pred == "Psoriasis" :
                st.subheader("Precautions")
                st.text(
                    """
                    1) Use moisturizing lotions.
                    2) Take care of your skin and scalp.
                    3) Avoid Dry, Cold Weather.
                    4) Use a humidifier.
                    5) Avoid medications that Cause flare-ups
                    6) Avoid scrapes, cuts, bumps, and infections.
                    7) Get some sun, but not too much.
                    """
                    )
                st.subheader("Home Remedy")
                st.text(
                    """
                    1) Yoga Can Improve Psoriasis.
                    2) Apply Aloe vera gel.
                    3) Remove Dry Skin Cells By Applying Tea Tree Oil.
                    4) A lukewarm bath with Epsom salt, mineral oil, milk, or olive oil can soothe the itching and infiltrate scales 
                    and plaques. Oatmeal baths can also be very helpful and soothing for plaque psoriasis.
                    """
                    )
                st.subheader("Diet")
                st.text(
                    """
                    1) Eat a Diet With More Colorful Fruits and Vegetables.
                    2) Drink Water to Keep Skin Hydrated and Healthy.
                    3) Avoid Alchol
                    4) Turmeric has been found to help minimize psoriasis flare-ups. It can be taken in pill or supplement form, or 
                    sprinkled on your food.
                    """
                    )

        except:
            st.error("This is not Picture of skin disease")
        
        
    """
        st.subheader("To fill the Patient Form, please click on button below")
        form_button = False
        form_button = st.button("Fill Form", key="b2")
        if form_button == True:
            print("pressed_button")
            st.subheader("Patient Form")
            form.Pform()
    """