// @flow strict
import React from 'react';
import parseISO from 'date-fns/parseISO';
import format from 'date-fns/format';
import styles from './Meta.module.scss';

type Props = {
  date: string
};

const Meta = ({ date }: Props) => {
  const formattedDate = format(parseISO(date), 'd MMM yyyy');

  return (
    <div className={styles['meta']}>
      <p className={styles['meta__date']}>Published {formattedDate}</p>
    </div>
  );
};

export default Meta;
