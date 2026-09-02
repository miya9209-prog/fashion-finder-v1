import re
CATEGORY_WORDS={'티셔츠':('상의','티셔츠'),'티':('상의','티셔츠'),'니트':('상의','니트'),'셔츠':('상의','셔츠'),'블라우스':('상의','블라우스'),'맨투맨':('상의','맨투맨·후드'),'후드':('상의','맨투맨·후드'),'팬츠':('하의','팬츠'),'바지':('하의','팬츠'),'슬랙스':('하의','슬랙스'),'데님':('하의','데님'),'청바지':('하의','데님'),'스커트':('하의','스커트'),'치마':('하의','스커트'),'원피스':('원피스',None),'자켓':('아우터','자켓'),'재킷':('아우터','자켓'),'가디건':('아우터','가디건'),'점퍼':('아우터','점퍼'),'코트':('아우터','코트'),'패딩':('아우터','패딩'),'세트':('세트',None)}
CONCERNS={'팔뚝':'팔뚝커버','팔':'팔뚝커버','뱃살':'뱃살커버','배':'뱃살커버','옆구리':'옆구리커버','하체':'하체커버','허벅지':'하체커버','힙':'힙커버','엉덩이':'힙커버','체형커버':'체형커버'}
TPO={'출근':'출근','회사':'출근','오피스':'출근','모임':'모임','하객':'하객','여행':'여행','휴가':'여행','주말':'주말','데일리':'데일리'}
COLORS={'검정':'블랙','블랙':'블랙','화이트':'화이트','흰색':'화이트','아이보리':'아이보리','베이지':'베이지','브라운':'브라운','네이비':'네이비','블루':'블루','핑크':'핑크','그레이':'그레이'}
def parse_query(query,brands):
    q=(query or '').strip(); p={'raw':q}
    for brand in brands:
        if brand.lower() in q.lower(): p['brand']=brand; break
    for word,(major,middle) in CATEGORY_WORDS.items():
        if word in q: p['major_category']=major; p.update({'middle_category':middle} if middle else {}); break
    for word,tag in CONCERNS.items():
        if word in q: p['concern']=tag; break
    for word,tag in TPO.items():
        if word in q: p['tpo']=tag; break
    for word,color in COLORS.items():
        if word in q: p['color']=color; break
    if '88' in q: p['min_max_size']=88
    elif '77' in q: p['min_max_size']=77
    elif '66반' in q: p['min_max_size']=66.5
    elif '66' in q: p['size_contains']='66'
    elif '55' in q: p['size_contains']='55'
    if any(x in q for x in ['오늘출발','오늘 출발','당일발송','당일 발송','바로배송','바로 배송']): p['same_day']=True
    if 'BEST' in q.upper() or '베스트' in q: p['best']=True
    if '신상품' in q or 'NEW' in q.upper(): p['new']=True
    m=re.search(r'(\d+)\s*만원\s*이하',q)
    if m: p['max_price']=int(m.group(1))*10000
    return p

def filter_products(df,p):
    out=df.copy()
    if p.get('brand'): out=out[out['brand']==p['brand']]
    if p.get('major_category'): out=out[out['major_category']==p['major_category']]
    if p.get('middle_category'): out=out[out['middle_category']==p['middle_category']]
    if p.get('min_max_size'): out=out[out['max_size']>=float(p['min_max_size'])]
    if p.get('size_contains'): out=out[out['sizes'].str.contains(str(p['size_contains']),na=False)]
    if p.get('concern'):
        tag=p['concern']; out=out[out['body_concerns'].fillna('').str.len()>0] if tag=='체형커버' else out[out['body_concerns'].str.contains(tag,na=False)]
    if p.get('tpo'): out=out[out['tpo'].str.contains(p['tpo'],na=False)]
    if p.get('color'): out=out[out['color'].str.contains(p['color'],na=False)]
    if p.get('same_day'): out=out[out['same_day']==True]
    if p.get('max_price'): out=out[out['price']<=int(p['max_price'])]
    if p.get('best'): out=out[out['badge'].str.contains('BEST',na=False)]
    if p.get('new'): out=out[out['badge'].str.contains('NEW',na=False)]
    return out

def humanize_filters(p):
    labels=[]
    if p.get('brand'): labels.append(p['brand'])
    labels.append(p['middle_category']) if p.get('middle_category') else labels.append(p['major_category']) if p.get('major_category') else None
    if p.get('min_max_size'): labels.append(f"{int(p['min_max_size'])}까지")
    elif p.get('size_contains'): labels.append(p['size_contains'])
    if p.get('concern'): labels.append(p['concern'])
    if p.get('tpo'): labels.append(p['tpo']+'룩' if p['tpo']=='출근' else p['tpo'])
    if p.get('color'): labels.append(p['color'])
    if p.get('same_day'): labels.append('당일발송')
    if p.get('max_price'): labels.append(f"{int(p['max_price']/10000)}만원 이하")
    if p.get('best'): labels.append('BEST')
    if p.get('new'): labels.append('NEW')
    return labels
