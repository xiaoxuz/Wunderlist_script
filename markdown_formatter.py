# -*- coding: utf-8 -*-

class MarkdownFormatter:

    def generate_categories(self,category_list):
        categories = ''
        for category in category_list:
            categories += category + ','
        return '['+categories[:-1]+']'

    def generate_tags(self,tag_list):
        tags = ''
        for tag in tag_list:
            tags += tag + ','
        return '['+tags[:-1]+']'

    def generate_H1(self,content):
        return '# '+content

    def generate_H2(self,content):
        return '## '+content

    def generate_H3(self,content):
        return '### '+content

    def generate_H4(self,content):
        return '#### '+content

    def generate_H5(self,content):
        return '##### '+content

    def generate_H6(self,content):
        return '###### '+content

    def generate_list_item(self,list_item):
        return '- '+list_item

    def generate_link(self,content,url):
        return '['+content+']('+url+')'
    
