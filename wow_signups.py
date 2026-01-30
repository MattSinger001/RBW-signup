

import numpy as np
import pandas as pd
import json
import streamlit as st


st.set_page_config(layout="wide")
#st.set_page_config(base='light')

input_str = '''
{"date":"29-01-2026","signUps":[{"entryTime":1769387981,"specName":"Marksmanship","name":"Creamcicle/Droplock","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564202084466708","id":341702714,"position":15,"classEmoteId":"592446395596931072","userId":"513056308828700672","status":"primary"},{"entryTime":1769567888,"specName":"Feral","name":"Starx","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564172061900820","id":342013089,"position":23,"classEmoteId":"734439523328720913","userId":"189527084593315840","status":"primary"},{"entryTime":1769542702,"specName":"Fury","name":"Mightyarcher/Praisegaben","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564445215948810","id":341964354,"position":22,"classEmoteId":"734439523328720913","userId":"470442626131427328","status":"primary"},{"entryTime":1769349205,"name":"Rag/Gothlim","className":"Absence","id":341611677,"position":13,"classEmoteId":"612343589070045200","userId":"999831289995726930","status":"primary"},{"entryTime":1769390412,"specName":"Demonology","name":"Smalldemort","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564407001513984","id":341705945,"position":16,"classEmoteId":"592446395596931072","userId":"344533759972081665","status":"primary"},{"entryTime":1769147512,"specName":"Demonology","name":"Justin","roleName":"Tanks","roleEmoteId":"598989638098747403","className":"Tank","specEmoteId":"637564407001513984","id":341333686,"position":1,"classEmoteId":"878310168289505301","userId":"436809774009417728","status":"primary"},{"entryTime":1769175793,"specName":"Retribution","name":"Dadious","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564297953673216","id":341365426,"position":5,"classEmoteId":"734439523328720913","userId":"229724834827993088","status":"primary"},{"entryTime":1769419473,"specName":"Frost","name":"Thelsolidan/Ryujinyakka","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564231469891594","id":341738677,"position":18,"classEmoteId":"592446395596931072","userId":"223284875006967808","status":"primary"},{"entryTime":1769412706,"specName":"Affliction","name":"Vfactor","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564406984867861","id":341730923,"position":17,"classEmoteId":"592446395596931072","userId":"282711148787138560","status":"primary"},{"entryTime":1769656456,"specName":"Fury","name":"hurtylad","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564445215948810","id":342157321,"position":28,"classEmoteId":"734439523328720913","userId":"618103128679645290","status":"primary"},{"entryTime":1769193138,"specName":"Assassination","name":"Dola","className":"Tentative","specEmoteId":"637564351707873324","id":341419799,"position":8,"classEmoteId":"676284492754976788","userId":"610245716056604765","status":"primary"},{"entryTime":1769632764,"specName":"Fury","name":"Ananakki/Animauler","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564445215948810","id":342113832,"position":27,"classEmoteId":"734439523328720913","userId":"479471226046382105","status":"primary"},{"entryTime":1769166462,"specName":"Holy1","name":"Sparrowhawks","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564297622454272","id":341353015,"position":3,"classEmoteId":"734439523328720913","userId":"188125071926099968","status":"primary"},{"entryTime":1769716153,"specName":"Fury","name":"SunshineDaydream","className":"Bench","specEmoteId":"637564445215948810","id":342242938,"position":29,"classEmoteId":"612373441051361353","userId":"1353399902650241024","status":"primary"},{"entryTime":1769471566,"specName":"Balance","name":"Veskarr","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564171994529798","id":341853554,"position":19,"classEmoteId":"592446395596931072","userId":"261773694592876545","status":"primary"},{"entryTime":1769719588,"specName":"Holy","name":"Karate(Trívia)","className":"Bench","specEmoteId":"637564323530539019","id":342249983,"position":30,"classEmoteId":"612373441051361353","userId":"917099609082458112","status":"primary"},{"entryTime":1769624886,"specName":"Marksmanship","name":"Viry","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564202084466708","id":342095853,"position":25,"classEmoteId":"592446395596931072","userId":"265520056580964353","status":"primary"},{"entryTime":1769177760,"specName":"Holy1","name":"Butters","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564297622454272","id":341368752,"position":6,"classEmoteId":"734439523328720913","userId":"222921728978976769","status":"primary"},{"entryTime":1769150379,"specName":"Feral","name":"Pweepy","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564172061900820","id":341336684,"position":2,"classEmoteId":"734439523328720913","userId":"737845013660172338","status":"primary"},{"entryTime":1769171162,"specName":"Holy","name":"Squish","roleName":"Healers","roleEmoteId":"592438128057253898","className":"Healer","specEmoteId":"637564323530539019","id":341358843,"position":4,"classEmoteId":"898011741735235645","userId":"509519156043972608","status":"primary"},{"entryTime":1769628767,"specName":"Holy","name":"botting","roleName":"Healers","roleEmoteId":"592438128057253898","className":"Healer","specEmoteId":"637564323530539019","id":342105002,"position":26,"classEmoteId":"898011741735235645","userId":"316023925815509002","status":"primary"},{"entryTime":1769319194,"specName":"Fire","name":"Sadie","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564231239073802","id":341579353,"position":12,"classEmoteId":"592446395596931072","userId":"1190643374122876989","status":"primary"},{"entryTime":1769539554,"specName":"Protection","name":"Kulvo","roleName":"Tanks","roleEmoteId":"598989638098747403","className":"Tank","specEmoteId":"637564444834136065","id":341956875,"position":21,"classEmoteId":"878310168289505301","userId":"1328147416888901632","status":"primary"},{"entryTime":1769270229,"specName":"Assassination","name":"Bjoren","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Melee","specEmoteId":"637564351707873324","id":341503163,"position":11,"classEmoteId":"734439523328720913","userId":"218136966464667649","status":"primary"},{"entryTime":1769213146,"specName":"Shadow","name":"Stinky","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564323291725825","id":341437288,"position":9,"classEmoteId":"592446395596931072","userId":"208922011911716865","status":"primary"},{"entryTime":1769576321,"specName":"Discipline","name":"Yitties","className":"Bench","specEmoteId":"637564323442720768","id":342023507,"position":24,"classEmoteId":"612373441051361353","userId":"224765321825746944","status":"primary"},{"entryTime":1769231511,"specName":"Destruction","name":"Brodoswagins","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564406682877964","id":341456530,"position":10,"classEmoteId":"592446395596931072","userId":"601203822794244099","status":"primary"},{"entryTime":1769374104,"specName":"Marksmanship","name":"Curlybill/Ruff","className":"Bench","specEmoteId":"637564202084466708","id":341667183,"position":14,"classEmoteId":"612373441051361353","userId":"232277695562645504","status":"primary"},{"entryTime":1769472762,"name":"Nazrael","className":"Absence","id":341855605,"position":20,"classEmoteId":"612343589070045200","userId":"217875360585351168","status":"primary"},{"entryTime":1769183293,"specName":"Balance","name":"Madeia/Hantaichrist","roleName":"Dps","roleEmoteId":"592440132129521664","className":"Ranged","specEmoteId":"637564171994529798","id":341378949,"position":7,"classEmoteId":"592446395596931072","userId":"1098471245936332840","status":"primary"}],"color":"255,0,0","classes":[{"specs":[{"name":"Arms","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564445031399474"},{"name":"Fury","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564445215948810"},{"name":"Protection","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564444834136065"},{"name":"Protection1","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564297647489034"},{"name":"Holy1","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564297622454272"},{"name":"Retribution","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564297953673216"},{"name":"Guardian","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564171696734209"},{"name":"Combat","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564352333086720"},{"name":"Demonology","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564407001513984"},{"name":"Destruction","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"637564406682877964"},{"name":"Enhancement","roleName":"Tanks","roleEmoteId":"598989638098747403","limit":999,"emoteId":"936357056951222322"}],"name":"Tank","limit":999,"emoteId":"878310168289505301","type":"primary"},{"specs":[{"name":"Arms","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564445031399474"},{"name":"Fury","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564445215948810"},{"name":"Retribution","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564297953673216"},{"name":"Holy1","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564297622454272"},{"name":"Feral","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564172061900820"},{"name":"Assassination","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564351707873324"},{"name":"Combat","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564352333086720"},{"name":"Subtlety","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564352169508892"},{"name":"Survival","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564202130866186"},{"name":"Beastmastery","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564202021814277"},{"name":"Enhancement","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"936357056951222322"}],"name":"Melee","limit":999,"emoteId":"734439523328720913","type":"primary"},{"specs":[{"name":"Arcane","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564231545389056"},{"name":"Fire","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564231239073802"},{"name":"Frost","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564231469891594"},{"name":"Destruction","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564406682877964"},{"name":"Demonology","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564407001513984"},{"name":"Affliction","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564406984867861"},{"name":"Beastmastery","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564202021814277"},{"name":"Marksmanship","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564202084466708"},{"name":"Survival","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564202130866186"},{"name":"Balance","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564171994529798"},{"name":"Shadow","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564323291725825"},{"name":"Smite","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"887257034066653184"},{"name":"Elemental","roleName":"Dps","roleEmoteId":"592440132129521664","limit":999,"emoteId":"637564379595931649"}],"name":"Ranged","limit":999,"emoteId":"592446395596931072","type":"primary"},{"specs":[{"name":"Arcane","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564231545389056"},{"name":"Frost","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564231469891594"},{"name":"Discipline","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564323442720768"},{"name":"Holy","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564323530539019"},{"name":"Restoration","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564172007112723"},{"name":"Holy1","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564297622454272"},{"name":"Restoration1","roleName":"Healers","roleEmoteId":"592438128057253898","limit":999,"emoteId":"637564379847458846"}],"name":"Healer","limit":999,"emoteId":"898011741735235645","type":"primary"},{"specs":[],"name":"Late","limit":999,"emoteId":"612373443551297689","type":"default","effectiveName":"Late"},{"specs":[],"name":"Bench","limit":999,"emoteId":"612373441051361353","type":"default","effectiveName":"Bench"},{"specs":[],"name":"Tentative","limit":999,"emoteId":"676284492754976788","type":"default","effectiveName":"Tentative"},{"specs":[],"name":"Absence","limit":999,"emoteId":"612343589070045200","type":"default","effectiveName":"Absence"}],"roles":[{"name":"Dps","limit":999,"emoteId":"592440132129521664"}],"description":"1SR MS>OS","channelType":"text","title":"SE20","templateId":"wowsod","serverId":"1236853472973033482","leaderId":"436809774009417728","lastUpdated":1769740201,"displayTitle":"SE20","closingTime":1769740200,"leaderName":"Justin","advancedSettings":{"temp_voicechannel":"false","twelve_format":false,"notes_enabled":true,"limit_per_user":1,"date1_emote":"1124529967611523272","tentative_emote":"676284492754976788","apply_unregister":false,"show_content":true,"countdown2_emote":"858794526176444467","event_type":"interaction","deletion":"false","poll_order":"sorted","limit":9999,"mention_mode":false,"signups1_emote":"1124529971428339752","text_2":"default","bench_overflow":true,"show_emotes":true,"show_extra_specs":true,"banned_roles":"none","image":"none","thumbnail":"none","show_footer":true,"apply_specreset":true,"disable_reason":false,"text_1":"default","allow_duplicate":false,"temp_time":24,"forum_tags":"Event","show_classes":false,"alt_names":false,"time2_emote":"593930235658108939","preserve_order":"false","tp_profile":"none","force_reminders":"false","tp_deletion":"1","show_title":true,"leader_emote":"1124529969926779050","mentions":"none","show_info":true,"late_emote":"612373443551297689","create_discordevent":true,"show_counter":true,"show_banned":false,"thread_logging":false,"bench_emote":"612373441051361353","lower_limit":0,"opt_out":"none","color":"none","use_nicknames":true,"info_variant":"short","show_on_overview":true,"voice_channel":"none","duration":0,"pin_message":false,"create_thread":"false","spec_saving":true,"vacuum":false,"time1_emote":"1124529972883767398","defaults_pre_req":true,"poll_add_req":"none","deadline":"0","unregister_emote":"579506704518217739","horizontal_mode":false,"poll_add":false,"show_countdown":true,"dkp_include":"signed","date2_emote":"593930359985405983","reminder":"false","mention_leader":false,"bold_all":true,"custom":"none","specs_per_signup":1,"show_leader":true,"font_style":"3","signups2_emote":"593930418932285440","dkp_delay":"24","temp_role":"false","allowed_roles":"none","queue_bench":false,"show_roles":true,"date_variant":"local","response":"none","dkp_amount":0,"embed_profile":"false","lock_at_limit":true,"specreset_emote":"761163891144130560","12h_format":false,"disable_archiving":false,"countdown1_emote":"1124530049329139772","absence_emote":"612343589070045200","show_numbering":true,"show_allowed":false,"delete_thread":false,"tr_include":"signed","attendance":"true"},"startTime":1769740200,"channelName":"thursday-se-2️⃣0️⃣","id":"1464135496069283841","time":"18:30","endTime":1769740200,"announcements":[],"channelId":"1424819052546621560"}
'''

input_str = input_str.replace('\n','')




st.title('RBW Raid Signups (Based on order/class)')

json_input = st.text_area('Copy/paste the signup JSON here')

if json_input == '':
    json_input = input_str
    st.markdown('# Example Raid Signup from 1-29')
else:
    json_input = json_input.replace('\n','')
    
data = json.loads(json_input)


signups = data['signUps']


Sequential_signups = sorted(signups,key=lambda d: d['entryTime'])


Sequential_classes = sorted(Sequential_signups,key=lambda d: d['className'])

data_signup = pd.DataFrame(Sequential_signups)

data_classes = pd.DataFrame(Sequential_classes)
#pd_data['position'] = pd_data.index


chosen_data = data_classes[['name','className','specName','position']]


def color_specName(val):
    if val == 'Discipline' or val == 'Holy' or val == 'Shadow' :
        color = '#FFFFFF'
    elif val == 'Destruction' or val == 'Demonology' or val == 'Affliction':
        color = '#8788EE'
    elif val == 'Guardian' or val == 'Feral' or val == 'Balance' or val == 'Restoration':
        color = '#FF7C0A'
    elif val == 'Frost' or val == 'Fire' or val == 'Arcane':
        color = '#3FC7EB'
    elif val == 'Assassination' or val == 'Combat' or val == 'Subtlety':
        color = '#FFF468'
    elif val == 'Arms' or val == 'Fury' or val == 'Protection':
        color = '#C69B6D'
    elif val == 'Beast Matery' or val == 'Marksmanship' or val == 'Survival':
        color = '#AAD372'
    elif val == 'Holy1' or val == 'Protection1' or val == 'Retribution':
        color = '#F48CBA'
    else:
        color = '#C41E3A'
    
    return f'background-color: {color}; color:black'

def color_text(val):
    return('color: black')

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown('# Tanks')
    temp_data = chosen_data[chosen_data['className']== 'Tank'] 
    temp_data = temp_data[['name','specName','position']]
    st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)

with col2:
    st.markdown('# Healers')
    temp_data = chosen_data[chosen_data['className']== 'Healer'] 
    temp_data = temp_data[['name','specName','position']]
    st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)

with col3:
    st.markdown('# Melee')
    temp_data = chosen_data[chosen_data['className']== 'Melee'] 
    temp_data = temp_data[['name','specName','position']]
    st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)

with col4:
    st.markdown('# Ranged')
    temp_data = chosen_data[chosen_data['className']== 'Ranged']
    temp_data = temp_data[['name','specName','position']]
    st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)

st.markdown('# Tentative')
temp_data = chosen_data[chosen_data['className']== 'Tentative']
temp_data = temp_data[['name','specName','position']]
st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)

st.markdown('# Absence')
temp_data = chosen_data[chosen_data['className']== 'Absence']
temp_data = temp_data[['name','specName','position']]
temp_data['specName'] = 'Not Avaliable'
st.dataframe(temp_data.style.applymap(color_specName, subset=['specName']),use_container_width=True,height=(len(temp_data) + 1) * 35 + 3)


































