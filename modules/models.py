from PyQt5.QtSql import (
    QSqlTableModel, QSqlRelationalTableModel, QSqlRelationalDelegate,
    QSqlQueryModel,
    QSqlQuery, QSqlRelation, QSqlIndex
)
from PyQt5.QtCore import Qt, QDate, QDateTime, QLocale

from PyQt5.QtWidgets import  QMessageBox

class DataModels:
    def __init__(self):
        self.kunden_model = QSqlQueryModel()
        self.initialize_model_kundenauswahl()

        self.owned_animals_model = QSqlQueryModel()
        self.initialize_model_owned_animals()

        self.treatment_selection_model = QSqlTableModel()
        self.initialize_treatment_selection_model()

        self.treatment_model = QSqlTableModel(self.treatment_selection_model)

        self.treatment_diagnosis_model = QSqlRelationalTableModel()

        self.treatment_service_model = QSqlRelationalTableModel()

        self.treatment_medics_model = QSqlRelationalTableModel()
        self.initialize_treatment_medic_model()

    def initialize_model_kundenauswahl(self):
        self.kunden_model.setHeaderData(0, Qt.Horizontal, "Relakey")
        self.kunden_model.setHeaderData(1, Qt.Horizontal, "Kundennummer")
        self.kunden_model.setHeaderData(2, Qt.Horizontal, "Anrede")
        self.kunden_model.setHeaderData(3, Qt.Horizontal, "Vorname")
        self.kunden_model.setHeaderData(4, Qt.Horizontal, "Name")
        self.kunden_model.setHeaderData(5, Qt.Horizontal, "Ort")
        self.kunden_model.setHeaderData(6, Qt.Horizontal, "search_string")

    def initialize_model_owned_animals(self):
        self.owned_animals_model.setHeaderData(0, Qt.Horizontal, "DisplayName")
        self.owned_animals_model.setHeaderData(1, Qt.Horizontal, "Relakey")
        self.owned_animals_model.setHeaderData(2, Qt.Horizontal, "CustomerRelakey")
        self.owned_animals_model.setHeaderData(3, Qt.Horizontal, "AnimalOrderNumber")
        self.owned_animals_model.setHeaderData(4, Qt.Horizontal, "AnimalName")
        self.owned_animals_model.setHeaderData(5, Qt.Horizontal, "Species")
        self.owned_animals_model.setHeaderData(6, Qt.Horizontal, "Race")
        self.owned_animals_model.setHeaderData(7, Qt.Horizontal, "Sex")

    def initialize_treatment_selection_model(self):
        self.treatment_selection_model.setTable('Behandlung')

    def initialize_treatment_medic_model(self):
        self.treatment_medics_model.setTable('Beh_Medikamente')

    def set_treatment_model(self, animalid):
        self.treatment_selection_model.setTable('Behandlung')
        self.treatment_selection_model.setFilter(f'ID_Tier = {animalid}')
        self.treatment_selection_model.select()

    def set_treatment_diagnosis_module(self, treat_id):
        self.treatment_diagnosis_model.setTable('Beh_Diagnosen')
        self.treatment_diagnosis_model.setFilter(f'ID_Behandlung = {treat_id}')
        self.treatment_diagnosis_model.setRelation(2, QSqlRelation('Diagnosen', 'ID_Diagnosen', 'Diagnose'))
        self.treatment_diagnosis_model.setJoinMode(QSqlRelationalTableModel.JoinMode(1))
        self.treatment_diagnosis_model.setSort(3, Qt.SortOrder(0))
        self.treatment_diagnosis_model.select()

    def set_treatment_service_module(self, treat_id):
        self.treatment_service_model.setTable('Beh_Leistungen')
        self.treatment_service_model.setFilter(f'ID_Behandlung = {treat_id}')
        self.treatment_service_model.setRelation(2, QSqlRelation('GOT_Leistungen', 'ID', 'Text'))
        self.treatment_service_model.setJoinMode(QSqlRelationalTableModel.JoinMode(1))
        self.treatment_service_model.setSort(4, Qt.SortOrder(0))
        self.treatment_service_model.select()

    def set_treatment_medics_model(self, treat_id):
        self.treatment_medics_model.setTable('Beh_Medikamente')
        self.treatment_medics_model.setFilter(f'ID_Behandlung = {treat_id}')
        self.treatment_medics_model.setRelation(2, QSqlRelation('Medikamente', 'ID_Medikament', 'Medi'))
        self.treatment_medics_model.setJoinMode(QSqlRelationalTableModel.JoinMode(1))
        self.treatment_medics_model.setSort(4, Qt.SortOrder(0))
        self.treatment_medics_model.select()

    def get_animals_from_customer(self, customerid):
        if customerid:
            query = QSqlQuery()
            query.prepare(
                'Select concat(name," ", if (isnull(T.Tierart),"",T.Tierart)," ",if (isnull(R.Rasse),"",R.Rasse)) '
                'as DisplayName, ID_Tier, ID_Kunde, TierNr, Name, T.Tierart, R.Rasse, G.Geschlecht  '
                'FROM  Tiere  LEFT JOIN Tierarten T on Tiere.Tierart = T.ID_Tierarten  '
                'LEFT JOIN Rasse R on Tiere.Rasse = R.ID_Rasse  '
                'LEFT JOIN Geschlecht G on Tiere.Geschlecht = G.ID_Geschlecht  '
                'WHERE ID_Kunde = :id '
                'ORDER BY Tot,  Verkauft , Name ')
            query.bindValue(":id", customerid)
            qok = query.exec_()
            if qok:
                self.owned_animals_model.setQuery(query)

            else:
                error = query.lastError().text()
                QMessageBox.critical(self, 'DatabaseError', f'Database Error \n\n {error}')

    def evt_on_kunden_searchtext_change(self, text):
        query = QSqlQuery()
        if text:
            query.prepare(
                'select `Patientenbesitzer`.`relakey` AS `relakey`,`Patientenbesitzer`.`kundennr` AS `kundennr`,\
                `Anrede`.`anrede` AS `Anrede`,`Patientenbesitzer`.`vorname` AS `vorname`,\
                `Patientenbesitzer`.`name` AS `name`,`Orte`.`ort` AS `Ort` \
                from ((`Patientenbesitzer` \
                left join `Orte` on(`Orte`.`relakey` = `Patientenbesitzer`.`ort`)) \
                left join `Anrede` on(`Anrede`.`idanrede` = `Patientenbesitzer`.`anrede`)) \
                left join Tiere on Tiere.ID_Kunde = Patientenbesitzer.relakey\
                WHERE lower(concat(Patientenbesitzer.name," ",Patientenbesitzer.vorname," ",Orte.ort ," ", Tiere.Name))\
                 like ? or lower(concat(Patientenbesitzer.name," ",Orte.ort ," ", Tiere.Name)) like ?\
                ORDER BY Patientenbesitzer.name')
            query.addBindValue("%{}%".format(text))
            query.addBindValue("%{}%".format(text))
        else:
            query.prepare(
                'select `Patientenbesitzer`.`relakey` AS `relakey`,`Patientenbesitzer`.`kundennr` AS `kundennr`,\
                `Anrede`.`anrede` AS `Anrede`,`Patientenbesitzer`.`vorname` AS `vorname`,\
                `Patientenbesitzer`.`name` AS `name`,`Orte`.`ort` AS `Ort` \
                from ((`Patientenbesitzer` \
                left join `Orte` on(`Orte`.`relakey` = `Patientenbesitzer`.`ort`)) \
                left join `Anrede` on(`Anrede`.`idanrede` = `Patientenbesitzer`.`anrede`))')
        qok = query.exec_()
        if qok:
            self.kunden_model.setQuery(query)
        else:
            QMessageBox.critical(self, 'DatabaseError', f'Database Error \n\n {query.lastError().text()}')