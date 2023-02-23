import utils
import read_csv
import charts



def run():
    namecountry = 'pblacion mundial'
    data = read_csv.read_csv('data.csv')
    
    que_ver = input('quieres ver la poblacion_mundial o un_pais ')
    if que_ver == 'un_pais':
        namecountry = input('type country =>')
 
        result = utils.population_by_country(data, namecountry)

        if len(result) > 0:
            country = result[0]
            labels, values = utils.get_population(country)
            print(labels, values)
            charts.generate_bar_chart(namecountry, labels, values)
            charts.generate_pie_chart(namecountry, labels, values)
    elif que_ver == 'poblacion_mundial':
        labels, values = utils.country_percentage(data)
        charts.generate_pie_chart(labels, values, namecountry)



if __name__ == '__main__':
    run()