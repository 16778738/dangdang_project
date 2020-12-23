
import os,django
from datetime import datetime, timedelta

from django.test import TestCase

# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()

from user.models import TBook,TCategory

# TCategory.objects.create(category_id="教育",level=1)
# TCategory.objects.create(category_id="小说",level=1)
# TCategory.objects.create(category_id="文艺",level=1)
# TCategory.objects.create(category_id="童书",level=1)
# TCategory.objects.create(category_id="电子书",level=1)
# TCategory.objects.create(category_id="生活",level=1)
# TCategory.objects.create(category_id="经管",level=1)
# TCategory.objects.create(category_id="励志",level=1)
# TCategory.objects.create(category_id="科技",level=1)

#
#
# TCategory.objects.create(category_id="教材",parent_id=1,level=2)
# TCategory.objects.create(category_id="外语",parent_id=1,level=2)
# TCategory.objects.create(category_id="考试",parent_id=1,level=2)
# TCategory.objects.create(category_id="中小学教辅",parent_id=1,level=2)
# TCategory.objects.create(category_id="工具书",parent_id=1,level=2)
#
# TCategory.objects.create(category_id="文学",parent_id=2,level=2)
# TCategory.objects.create(category_id="转机",parent_id=2,level=2)
# TCategory.objects.create(category_id="艺术",parent_id=2,level=2)
# TCategory.objects.create(category_id="摄影",parent_id=2,level=2)
#
# TCategory.objects.create(category_id="历史",parent_id=3,level=2)
# TCategory.objects.create(category_id="两性",parent_id=3,level=2)
# TCategory.objects.create(category_id="保健",parent_id=3,level=2)




# time = datetime.now().date()- timedelta(days=365)
# print(time)

# TBook.objects.create(book_name="给教师的建议·精装",author="B.A.苏霍姆林斯基",publish="长江文艺出版社",publish_time="2014-12月", isbn="97875",word_count="345360",page_count="42342",category_id="10",old_price="38.00",new_price="33.70", content_introduction="苏霍姆林斯基国内无删减、全译版。成就优秀教师的必备经典。顾明远，周国平，朱永新真诚推荐！ 助力开学,中小学教辅每满100减50 ",picture="01.png")
# TBook.objects.create(book_name="可爱的中国",author="方志敏",publish="陕西师范大学出版社",publish_time="2018-12月", isbn="97873",word_count="345360",page_count="4232242",category_id="13",old_price="46.00",new_price="36.00", content_introduction="在新中国成立70周年、方志敏同志诞辰120周年之际，中央一套播出电视剧《可爱的中国》，本书收录《可爱的中国》《清贫》等文，深度体现方志敏的革命气节和崇高风范。 ",picture="04.png")
# TBook.objects.create(book_name="读图识中国",author="人民教育出版社地图编辑室",publish="人民教育出版社",publish_time="2009-03月", isbn="97873",word_count="345360",page_count="4232242",category_id="13",old_price="46.00",new_price="36.00", content_introduction="入选教育部中小学生阅读指导目录 推荐阅读插画本儿童知识地图集 助力开学,中小学教辅每满100减50 ",picture="05.png")
# TBook.objects.create(book_name="理想国",author="柏拉图",publish="商务印书馆",publish_time="2020年06月", isbn="978038",word_count="299919",page_count="30020", book_paper="胶版纸",category_id="1",old_price="68.5",new_price="34.99", content_introduction="《理想国》是柏拉图的一篇重要对话录，涉及柏拉图思想体系的各个方面，包括哲学、伦理、教育、文艺、政治等内容",picture="1.jpg")
# TBook.objects.create(book_name="混知健康日历",author="陈磊",publish="商务印书馆",publish_time="2020年08月", isbn="2230438",word_count="199929",page_count="25002", book_paper="胶版纸",category_id="6",old_price="28.78",new_price="50.88", content_introduction="",picture="03.png")
#
# TBook.objects.create(book_name="聪明宝宝入园攻略",author="蓝草帽",publish="阳光出版社",publish_time="2019年06月", isbn="279735",word_count="23300",page_count="35312", book_paper="铜版纸",category_id="4",old_price="68.2",new_price="168", content_introduction="缓解入园焦虑 分离焦虑 培养孩子独立性（童立方蓝草帽出品）",picture="01.png")
# TBook.objects.create(book_name="结构性改革",author="黄奇帆",publish="中信出版社",publish_time="2020年08月", isbn="787145",word_count="234300",page_count="50482", book_paper="纯质纸",category_id="7",old_price="59.0",new_price="88.88", content_introduction="针对当前中国经济面临的一系列难题，本书提出了可行的解决思路和方案。作者长期从事经济工作，实践经验丰富。适合经济工作者、行政部门、企业经管阅读 ",picture="5.jpg")
#
# TBook.objects.create(book_name="现代汉语词典",author="中国社会科学院语言研究所词典编辑室",publish="商务印书馆",publish_time="2016年09月", isbn="986508",word_count="923300",page_count="75312", book_paper="胶版纸",category_id="1",old_price="93",new_price="109", content_introduction="《现代汉语词典》自1978年正式出版以来做过多次修订，以适应社会的发展，更好地反映现代汉语词汇新面貌，体现有关学科研究的新成果，落实国家有关语言文字方面的新规范。",picture="4.jpg")
# TBook.objects.create(book_name="星火英语四级真题试卷备考",author="汪开虎",publish="上海交通大学出版社",publish_time="2020年01月", isbn="776709",word_count="345360",page_count="42342", book_paper="胶版纸",category_id="1",old_price="36.8",new_price="59.8", content_introduction="星火英语四级真题试卷备考2020年9月全套资料大学英语cet4历年真题模拟 词汇听力阅读理解写作文专项训练书",picture="3.jpg")
#
