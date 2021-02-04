import sqlite3

def main():
    conn = sqlite3.connect('surrey.db')
    c = conn.cursor()
    
    try:
        # Create tables
        c.execute('''CREATE TABLE waiting_points (id integer PRIMARY KEY AUTOINCREMENT, region text, lon integer, lat integer)''')
        c.execute('''CREATE TABLE demand_points (id integer PRIMARY KEY AUTOINCREMENT, region text, lon integer, lat integer, crime_index real, population_index real)''')
        c.execute('''CREATE TABLE distances (w_id integer, d_id integer, distance_km real, time_m real)''')
        c.execute('''CREATE TABLE optomization_output (n integer, alpha_i integer, )''') 
    except Exception as e:
        raise(e)
    finally:
        # close connection and cursor
        c.close()
        conn.close()

if __name__ == "__main__":
    main()